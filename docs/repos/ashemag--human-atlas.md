---
title: ashemag/human-atlas
source: https://github.com/ashemag/human-atlas
stars: 1695
category: Web & Frontend
---

# ashemag/human-atlas

- **URL**: https://github.com/ashemag/human-atlas
- **Stars**: 1695
- **Language**: TypeScript
- **Category**: Web & Frontend
- **Topics**: None

## What it does
Human Atlas is an interactive 3D anatomy explorer that allows users to view and interact with 2,234 selectable BodyParts3D meshes across 15 anatomical systems. Users can search for anatomical names and inspect details of individual structures.

## Why it's interesting
Unlike typical anatomy applications, Human Atlas offers a highly interactive experience with a focus on web technologies like React and Three.js, enabling real-time manipulation of 3D models directly in the browser without requiring additional software or plugins.

## How it works
The application merges geometry into batches for efficient rendering, using GPU textures for visibility and selection. It supports various layouts for desktop and mobile, ensuring responsive controls. Validation scripts check for mesh integrity and interaction performance, although physical-device performance has not been tested. The anatomy data is based on BodyParts3D 4.0 and is simplified for browser performance.

## Get started in 5 minutes
1. Clone the repository.
2. Ensure you have Node.js 22.13 or newer.
3. Run `npm ci` to install dependencies.
4. Start the development server with `npm run dev` and open http://localhost:3016 in your browser.

## Watch out for
The project is relatively new, created in September 2026, and may lack extensive community support. The anatomy data is licensed under CC BY 4.0, requiring proper attribution for redistribution. Performance on physical devices has not been validated, which may affect usability in real-world scenarios.
