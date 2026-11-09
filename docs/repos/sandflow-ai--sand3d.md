---
title: Sandflow-ai/sand3d
source: https://github.com/Sandflow-ai/sand3d
stars: 1562
category: Developer Tools
---

# Sandflow-ai/sand3d

- **URL**: https://github.com/Sandflow-ai/sand3d
- **Stars**: 1562
- **Language**: HTML
- **Category**: Developer Tools
- **Topics**: 3d, blender, cad, llm, procedural-modeling, python, usd

## What it does
sand3d is a Python library designed for 3D modeling, allowing users to create 3D objects through programmatic definitions. It integrates with Blender's `bpy` module and enables the export of models in various formats such as GLB, URDF, USD, OBJ, and STL.

## Why it's interesting
Unlike traditional 3D modeling tools that rely heavily on manual manipulation, sand3d allows for the creation of 3D objects using concise, readable code. This approach can significantly reduce the amount of code needed to define complex shapes, making it more accessible for users who prefer programming over graphical interfaces.

## How it works
The library operates by defining 3D objects as programs that describe their components and relationships, using a straightforward API. It emphasizes determinism, meaning the same code will produce the same output consistently. The README provides examples of how to create objects and export them in multiple formats, but it does not detail the underlying architecture or any specific algorithms used in the library.

## Get started in 5 minutes
To get started, ensure you have Python 3.11 or 3.13 installed. Then, install sand3d using the command:
```bash
pip install sand3d
```
You can then create a simple 3D object by importing the library and defining a function, as shown in the provided example for creating a bracket.

## Watch out for
The repository is relatively new, created in November 2026, which may imply limited community support and potential bugs. Additionally, the library relies on Blender's `bpy`, which may have compatibility issues with certain Python versions or platforms (e.g., Intel Macs). The licensing is under Apache 2.0, which is permissive but requires attribution.
