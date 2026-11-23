---
title: ItsNotRexed/Leonida
source: https://github.com/ItsNotRexed/Leonida
stars: 22827
category: Other
---

# ItsNotRexed/Leonida

- **URL**: https://github.com/ItsNotRexed/Leonida
- **Stars**: 22827
- **Language**: Python
- **Category**: Other
- **Topics**: None

## What it does
Leonida is a project aimed at recompiling the Xbox Series version of Grand Theft Auto VI to run natively on Windows PCs. It allows users to utilize their own game files to build and run the game, translating console-specific code and assets for PC compatibility.

## Why it's interesting
Unlike traditional emulators, Leonida focuses on static recompilation, leveraging the similarities between the Xbox Series and PC architectures. This approach aims to achieve better performance and compatibility by running the game natively rather than simulating the console environment.

## How it works
The project reimplements the Xbox console's system software and translates precompiled GPU programs to SPIR-V for Vulkan. It currently supports shader translation, model and texture extraction, and basic runtime functionality, but the game itself does not boot yet. The README indicates that while many components are in place, significant work remains to achieve a playable state, particularly regarding the integration of the game's executable and complete functionality of the D3D12 to Vulkan layer.

## Get started in 5 minutes
To get started, clone the repository with its submodules using `git clone --recursive https://github.com/ItsNotRexed/Leonida`, ensure you have the necessary prerequisites installed, and then run `Build.bat` to initiate the build process. The build script automatically locates your copy of the game and checks for required dependencies.

## Watch out for
The project is still in early development, with the game not yet booting. Users must have their own copy of the Xbox Series game files, and the repository does not provide any game assets or executables. Additionally, the README outlines a significant disk space requirement (around 400 GB) for the build process, which may be a barrier for some users.
