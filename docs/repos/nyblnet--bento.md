---
title: nyblnet/bento
source: https://github.com/nyblnet/bento
stars: 1306
category: Web & Frontend
---

# nyblnet/bento

- **URL**: https://github.com/nyblnet/bento
- **Stars**: 1306
- **Language**: TypeScript
- **Category**: Web & Frontend
- **Topics**: None

## What it does
Bento is a self-contained office suite that allows users to create, edit, and present slides as a single HTML file. It includes features like live collaboration, built-in charts, and a local-first approach, meaning all data is stored within the file itself.

## Why it's interesting
Unlike traditional office suites that require installation and often rely on cloud services, Bento operates entirely offline and is distributed as a single file. This eliminates vendor lock-in and ensures that users have full control over their documents, which are stored in a readable JSON format.

## How it works
Bento's architecture is based on a single-page application built with TypeScript. The document model is defined in `slides/src/model.ts`, and it utilizes a custom CRDT for real-time collaboration. The app can be built from source using Node.js and npm, and it supports offline functionality through the File System Access API. The README does not specify the exact technologies used for the rendering engine or the collaboration features, leaving some uncertainty about the underlying implementations.

## Get started in 5 minutes
To try Bento, download the `Bento_Slides.bento.html` file from the [GitHub Releases](https://github.com/nyblnet/bento/releases) or from [bento.page](https://bento.page/releases/slides/Bento_Slides.bento.html). Open the file in any modern browser to start using the editor and presentation features.

## Watch out for
The repository was created in July 2026, indicating it is relatively new and may still be in active development. Users should be aware of potential bugs or missing features as the project matures. Additionally, while the app is open source under the MIT License, users should review the licensing of bundled components and embedded typefaces for compliance.
