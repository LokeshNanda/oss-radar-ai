---
title: wy51ai/floorplan-3d
source: https://github.com/wy51ai/floorplan-3d
stars: 1412
category: Web & Frontend
---

# wy51ai/floorplan-3d

- **URL**: https://github.com/wy51ai/floorplan-3d
- **Stars**: 1412
- **Language**: HTML
- **Category**: Web & Frontend
- **Topics**: None

## What it does
This repository provides a front-end tool for designing floor plans in 2D and 3D. Users can place furniture, modify walls, and measure dimensions, with the ability to switch to a 3D view using Three.js for a more immersive experience.

## Why it's interesting
Unlike many similar applications, this tool is entirely front-end and requires no build process, making it accessible for quick use. It also allows for real-time synchronization between 2D and 3D views, which is not commonly found in simpler design tools.

## How it works
The application is built using HTML, CSS, and JavaScript without any frameworks. It utilizes SVG for 2D rendering and Three.js for 3D visualization. Users can customize floor plans directly in the `index.html` file by modifying predefined data structures for rooms, walls, materials, and furniture. The application saves user data in the browser's localStorage, and it loads Three.js via a CDN, requiring an internet connection for the first 3D scene load.

## Get started in 5 minutes
Clone the repository and navigate to the directory:
```bash
git clone <仓库地址>
cd <仓库目录>
```
Then, open `index.html` in a web browser or start a local static server:
```bash
python3 -m http.server 8000
# Access at http://localhost:8000
```

## Watch out for
The repository lacks a description and topics, which may hinder discoverability. The README does not mention any testing or known issues, so users should be cautious about potential bugs. Additionally, since it relies on localStorage, data may be lost if the browser's storage is cleared. The project is licensed under MIT, which allows for modification and redistribution.
