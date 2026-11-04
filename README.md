<div align="center">

# NEXORA OS

### A modern desktop experience. Built to be yours.

**A customizable, application-driven desktop environment with a focus on design, productivity, creativity, and development.**

[Website](https://nexora-tech26.github.io/Nexora/) · [Releases](https://github.com/Nexora-Tech26/Nexora/releases) · [Issues](https://github.com/Nexora-Tech26/Nexora/issues) · [Nexora Store Catalog](https://github.com/Nexora-Tech26/Nexora/tree/main/nexora-store)

</div>

---

## Meet Nexora

**Nexora OS** is an independent desktop-environment project exploring what a modern, personal computing experience can look like. It combines an original interface, a growing collection of built-in tools, an application Store, and a platform for creating and distributing Nexora applications.

The project is designed around one idea: **your desktop should adapt to you, not the other way around.**

Nexora emphasizes polished visuals, practical workflows, a connected interface, and opportunities for developers to build new experiences within its ecosystem.

> **What Nexora is today:** Nexora is primarily a Python/Qt-based desktop shell and application platform that runs on top of an existing operating system. It is **not currently a standalone replacement operating system with its own kernel and bootloader**. A fully independent OS remains a longer-term ambition rather than a shipped capability.

## Highlights

| Experience | What it offers |
| --- | --- |
| **Nexora Desktop** | A custom desktop, navigation, panels, window management concepts, and a unified visual language. |
| **Personalization** | Themes, backgrounds, visual effects, and interface settings designed to make Nexora feel personal. |
| **Built-in Applications** | Everyday tools such as Files, Settings, Notepad, Calculator, Calendar, Terminal, and Clock. |
| **Nexora Store** | A developing ecosystem for discovering, installing, and updating compatible application packages. |
| **Developer Tools** | Code editing, project workflows, NexoraScript, and export of Nexora application packages. |
| **Application Packages** | Manifest-based applications distributed in ZIP archives or compatible folders. |
| **Update Infrastructure** | Versioned application catalogs and work toward verified, full-release system updates. |
| **Cross-platform Direction** | Development targeting Windows, macOS, and Linux, with platform-specific differences and testing still required. |

## A Desktop With Its Own Identity

Nexora's interface is designed to feel cohesive from startup to shutdown.

Its design direction includes:

- A modern, rounded UI with carefully balanced spacing.
- Translucent and glass-inspired surfaces where they improve readability.
- A recognizable violet, pink, and orange gradient identity.
- Consistent icons, buttons, controls, panels, and settings screens.
- Smooth transitions and subtle motion.
- Integrated desktop, launcher, notifications, and control-center experiences.
- Keyboard shortcuts and workflows intended to keep everyday tasks close at hand.

Some UI features are implemented and others are under active refinement. Performance, consistency, and accessibility remain ongoing priorities.

## Applications for Everyday Work

Nexora brings together essential utilities in one environment:

- **Files** — browse and manage local files.
- **Settings** — customize the desktop and system experience.
- **Notepad** — create and edit text documents.
- **Calculator** — perform everyday calculations.
- **Calendar** — organize dates and schedules.
- **Terminal** — access command-line workflows.
- **Clock** — time-related tools and utilities.

The larger Nexora ecosystem also explores application collections for **developers, servers, business, creative work, and device utilities**. Availability and maturity vary between bundled apps and packages published online.

## Nexora Store

The Nexora Store is intended to make Nexora expandable without requiring a complete desktop rebuild whenever a new application is introduced.

The application architecture supports a manifest-based workflow:

1. A developer prepares an application and its metadata.
2. The application is packaged for distribution.
3. The Store reads the public catalog and checks compatible package information.
4. The package is downloaded, validated, and installed into its own application directory.
5. Nexora discovers compatible installed applications through their manifests.
6. Later versions can be distributed independently through Store updates.

**Important:** The public catalog and app packaging infrastructure are available, but not every bundled Nexora app is published online, and update behavior still requires end-to-end validation across supported platforms.

### Developer Pack and Code Editor PRO

Nexora aims to make application development part of the desktop experience.

**Code Editor PRO** provides a development workspace for Python-based Nexora projects, including multi-file editing, project browsing, syntax checking, running code, importing ZIP projects, and exporting application packages with a selectable main entry point.

**NexoraScript** is integrated **inside Code Editor PRO**. It is a Python-derived syntax that translates into Python rather than a separate operating-system programming language or a separate Store app.

The intended path is straightforward:

```text
Create a project
      |
Write Python or NexoraScript
      |
Choose the startup file
      |
Export a Nexora application ZIP
      |
Install locally or prepare a Store release
```

Exporting a package does **not** automatically publish it to the public Store; repository publication and release verification are separate steps.

## Updates and Reliability

Nexora is developing two distinct update paths:

**Application updates** are intended to distribute individual application packages through the Store without replacing the full desktop environment.

**Nexora system updates** are intended to use complete release archives. The updater is designed to validate downloads, back up program files, replace application components, and preserve recognized user-data locations.

A complete release package makes it possible to design upgrades without depending on every intermediate version. However, **automatic relaunch, preservation of every possible custom data location, and full cross-platform update reliability are not yet guaranteed**. Back up important files before testing a system update.

## Technology

Nexora's current desktop implementation is built primarily with:

- **Python** for application and desktop logic.
- **PySide6 / Qt** for graphical interfaces.
- **JSON** for selected configuration, manifests, and catalogs.
- **ZIP packages** for distribution of compatible applications and releases.
- **GitHub** for source hosting, releases, and the public Store catalog.

Platform-specific functionality may require additional dependencies. Consult the files shipped with the relevant release for its startup and installation instructions.

## Current Status

**Nexora is an evolving project.** Parts of the interface and application framework are usable, while other areas are experimental or still being improved.

| Area | Status |
| --- | --- |
| Python/Qt desktop shell | In development |
| Built-in desktop utilities | Implemented in varying degrees |
| Store application catalog | Public catalog available |
| Manifest-based app packaging | Implemented; compatibility varies |
| Code Editor PRO and NexoraScript | Available as a published Store package |
| Full system update distribution | Infrastructure under development |
| Fully independent kernel-based OS | Future direction; not shipped |

See [Releases](https://github.com/Nexora-Tech26/Nexora/releases) for downloadable builds. The existence of a version number or update-feed file does not necessarily mean that a corresponding full release has been uploaded.

## Project Direction

The long-term direction for Nexora includes:

- More capable and consistent desktop applications.
- Faster startup and better performance on a wider range of hardware.
- More complete keyboard and controller accessibility.
- Improved localization and translation coverage.
- A more polished and unified Store experience.
- More independent application releases and updates.
- More reliable system upgrades, backups, and recovery.
- Better Windows, macOS, and Linux compatibility.
- A broader platform for developers and creators.

These are development goals, not promises that each feature is already available.

## Getting Started

1. Open the [Releases page](https://github.com/Nexora-Tech26/Nexora/releases) and choose an available build.
2. Read the included release notes and platform requirements.
3. Download and extract the release archive.
4. Follow the startup instructions included with that build.
5. Test updates on a copy of your environment and back up important data.

> **Security note:** Nexora applications may contain executable Python code. Install packages only from sources you trust, review permissions and code when possible, and treat untrusted ZIP files as untrusted software.

## Feedback and Contributions

Nexora is an ambitious project that benefits from testing, bug reports, feature suggestions, design feedback, and contributions.

If you encounter a bug or have an idea, open an [issue](https://github.com/Nexora-Tech26/Nexora/issues). Include the version, operating system, expected behavior, actual behavior, and relevant logs when possible.

Before contributing code, check the current repository structure and existing discussions. Development conventions and APIs may change as the project evolves.

---

<div align="center">

### Create. Customize. Discover. Evolve.

**NEXORA OS — Built for what comes next.**

[Explore the project](https://github.com/Nexora-Tech26/Nexora) · [Report an issue](https://github.com/Nexora-Tech26/Nexora/issues)

</div>
