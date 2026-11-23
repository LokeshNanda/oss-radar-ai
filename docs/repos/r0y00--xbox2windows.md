---
title: R0Y00/Xbox2Windows
source: https://github.com/R0Y00/Xbox2Windows
stars: 1417
category: Developer Tools
---

# R0Y00/Xbox2Windows

- **URL**: https://github.com/R0Y00/Xbox2Windows
- **Stars**: 1417
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: d3d12, directx-raytracing, scarlett, static-recompilation, windows, xbox, xbox-series-x

## What it does
Xbox2Windows is a research project focused on static recompilation of Xbox Series X|S software to x64 Windows. It translates selected x64 machine code into C++ and graphics shaders into desktop DXIL, allowing for public tests without requiring a game installation.

## Why it's interesting
This project stands out due to its focus on translating console software for use on Windows, which is not commonly addressed by mainstream tools. It provides a unique approach to running Xbox titles on a PC by leveraging static recompilation techniques, which can be beneficial for developers interested in cross-platform compatibility.

## How it works
The architecture involves translating Xbox machine code and shaders into formats compatible with Windows. The README details various tests that have been conducted, including comparisons of output from native, mapped, and recompiled programs. However, the execution of full games and frame rates remains unverified, indicating that the project is still in a research phase.

## Get started in 5 minutes
To get started, clone the repository and run the following commands in PowerShell:
```powershell
git clone https://github.com/R0Y00/Xbox2Windows.git
cd Xbox2Windows
.
\tools\dev.ps1
python -m venv out/pe-env
.
\out\pe-env\Scripts\python.exe -m pip install -r requirements-dev.txt
cmake --preset dev
cmake --build --preset dev
ctest --preset dev --no-tests=error -R 'desktop_root_signature|era_heap_allocation|offscreen_warp'
```
This will set up the environment and run initial tests.

## Watch out for
The project is still in development, with certain features like full-game startup and frame rate verification remaining unverified. Additionally, it requires specific versions of tools like Python and Visual Studio, which may pose compatibility issues. There are no explicit licensing details mentioned in the README, so users should verify the project's licensing before use.
