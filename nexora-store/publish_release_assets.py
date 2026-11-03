"""Publish uploaded and verified GitHub Release ZIPs to Nexora's public update feeds."""
from __future__ import annotations
import hashlib
import json
import os
import re
import stat
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
ID = re.compile(r"[a-z0-9][a-z0-9._-]{1,63}\Z")
NEEDED = {"Nexora.py", "system/run.py", "system/nexora/app.py", "system/release.json"}

def check(path, limit):
    if path.stat().st_size > limit:
        raise ValueError("Package too large: " + path.name)
    with zipfile.ZipFile(path) as z:
        infos = z.infolist()
        if len(infos) > 30000 or sum(i.file_size for i in infos) > 8 * 1024 ** 3:
            raise ValueError("Archive exceeds extraction safety limits")
        for info in infos:
            p = PurePosixPath(info.filename)
            if not p.parts or p.is_absolute() or ".." in p.parts or stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError("Unsafe archive member")
        return set(z.namelist())

def metadata(path):
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        if "manifest.json" in names:
            check(path, 128 * 1024 ** 2)
            m = json.loads(z.read("manifest.json"))
            if not ID.fullmatch(str(m.get("id", ""))) or m.get("type", "app") != "app" or not m.get("version"):
                raise ValueError("Invalid Nexora application manifest")
            if not m.get("entrypoint") or m["entrypoint"] not in names:
                raise ValueError("Application entrypoint not found")
            return "app", m
        prefix = "" if NEEDED.issubset(names) else None
        if prefix is None:
            roots = {n.split("/",1)[0] for n in names if "/" in n}
            if len(roots) == 1:
                root = next(iter(roots)) + "/"
                if all(root+n in names for n in NEEDED): prefix = root
        if prefix is None: raise ValueError("Not a complete Nexora system release")
        check(path, 4 * 1024 ** 3)
        m = json.loads(z.read(prefix+"system/release.json"))
        if "nexora" not in str(m.get("product","")).lower() or not m.get("version"):
            raise ValueError("Invalid system metadata")
        return "system", m

def read(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default

def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

def publish(folder, tag, repo):
    if not re.fullmatch(r"[\w.\-]{1,100}", tag) or not re.fullmatch(r"[\w.\-]+/[\w.\-]+", repo):
        raise ValueError("Invalid tag or repository")
    catalog_path = ROOT/"catalog.json"
    feed_path = ROOT/"release-feed.json"
    catalog = read(catalog_path, {"schema":1,"apps":[],"packs":[]})
    feed = read(feed_path, {"format":"nexora.update-feed","version":1,"updates":[]})
    if catalog.get("schema") != 1 or feed.get("format") != "nexora.update-feed" or feed.get("version") != 1:
        raise ValueError("Unsupported catalog format")
    assets = sorted(folder.glob("*.zip"))
    if not assets: raise ValueError("No release ZIP assets")
    for asset in assets:
        kind, m = metadata(asset)
        with asset.open("rb") as f: sha = hashlib.file_digest(f,"sha256").hexdigest()
        url = f"https://github.com/{repo}/releases/download/{quote(tag)}/{quote(asset.name)}"
        if kind == "app":
            aid = m["id"]
            row = {"id":aid,"name":m.get("name",aid),"version":str(m["version"]),
                   "description":m.get("description",""),"category":m.get("category","Other"),
                   "publisher":m.get("publisher","Nexora Technologies"),"url":url,"sha256":sha}
            catalog["apps"] = [x for x in catalog["apps"] if x.get("id") != aid]+[row]
        else:
            channel = str(m.get("channel","stable")).lower()
            if channel == "preview":channel = "beta"
            if channel not in ("stable","beta","developer"):raise ValueError("Invalid update channel")
            version = str(m["version"])
            row = {"version":version,"channel":channel,"build_id":str(m.get("build",version)),
                   "url":url,"sha256":sha,"size":asset.stat().st_size,
                   "restart_required":True,"minimum_version":"0",
                   "published_at":datetime.now(timezone.utc).isoformat(timespec="seconds"),
                   "changelog":m.get("notes","Nexora complete system update")}
            feed["updates"] = [x for x in feed["updates"]
                               if (x.get("version"),x.get("channel")) != (version,channel)]+[row]
        print(kind,asset.name,sha)
    write(catalog_path,catalog)
    write(feed_path,feed)

if __name__ == "__main__":
    publish(Path(sys.argv[1]),sys.argv[2],os.environ["GITHUB_REPOSITORY"])
