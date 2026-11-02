---
title: patch-gg/pixelfx
source: https://github.com/patch-gg/pixelfx
stars: 3239
category: Web & Frontend
---

# patch-gg/pixelfx

- **URL**: https://github.com/patch-gg/pixelfx
- **Stars**: 3239
- **Language**: JavaScript
- **Category**: Web & Frontend
- **Topics**: agent-skills, animation, canvas, claude-code-plugin, gamedev, pixel-art, sprite-sheet, vfx

## What it does
The `pixelfx` repository provides 244 pixel art effects and animations, designed for use in browser games and other applications. It allows developers to easily integrate these effects into their projects, customize them, and even create new effects using a Claude Code skill.

## Why it's interesting
Unlike many other libraries that offer static assets, `pixelfx` focuses on dynamic, code-based effects that can be customized in real-time. The integration of a Claude Code skill for generating new effects sets it apart from traditional sprite libraries, enabling a more interactive and creative approach to game development.

## How it works
The library is structured around JavaScript files located in `src/fx/<category>/<name>.js`, where each effect is defined as a function that can be called to render animations. It uses a two-buffer system for color and light, allowing for complex visual effects without relying on image assets. Effects can be used directly in canvas-based games or exported as sprite sheets for various game engines. The README provides detailed examples of how to implement effects in a game loop and create new effects, although it does not specify the underlying architecture or performance benchmarks.

## Get started in 5 minutes
To quickly try `pixelfx`, install it via npm with the command `npm i github:patch-gg/pixelfx`. Then, use the provided example code to import an effect and integrate it into your game loop, or run `node tools/render.mjs ice/frost-nova --sheet` to generate a sprite sheet for use in other engines.

## Watch out for
The repository is relatively new, created in October 2026, which may imply that it is still evolving and could have undiscovered bugs or incomplete documentation. The effects are licensed under MIT, allowing for commercial use, but the README notes that some parts are adapted from other sources, which may have different licensing terms.
