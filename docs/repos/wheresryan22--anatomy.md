---
title: wheresryan22/anatomy
source: https://github.com/wheresryan22/anatomy
stars: 4847
category: Developer Tools
---

# wheresryan22/anatomy

- **URL**: https://github.com/wheresryan22/anatomy
- **Stars**: 4847
- **Language**: JavaScript
- **Category**: Developer Tools
- **Topics**: agent-skill, open-source, svg, vizualization

## What it does
Anatomy is an agent skill designed to create detailed, interactive isometric illustrations of real-world machines and complex systems. It generates polished SVGs and incorporates optional WebGL shaders and 3D effects to enhance visual representation.

## Why it's interesting
Anatomy stands out by allowing users to generate illustrations based on natural language prompts, transforming abstract concepts into physical representations. This capability is particularly useful for educational and technical documentation, where visual aids can significantly enhance understanding.

## How it works
The tool operates as an Agent Skill, leveraging Node.js and built-in modules without requiring external dependencies. Users can install it via the `npx skills` command and interact with it through agents like Claude Code, OpenCode, or Codex. The skill interprets user prompts to create illustrations that can include SVG, WebGL, and 3D elements, all rendered in a consistent isometric perspective. However, the README does not provide detailed information on the underlying algorithms or data structures used for generating the illustrations, leaving some uncertainty about its internal workings.

## Get started in 5 minutes
To quickly try Anatomy, run the following command in your terminal:
```sh
npx skills add wheresryan22/anatomy -g -a claude-code
```
Then, in Claude Code, you can use the command:
```text
/anatomy explain how a token bucket rate limiter works, interactive
```

## Watch out for
The repository is relatively new, created in October 2026, which may imply that it is still in active development and could have undiscovered bugs or incomplete features. Additionally, while it is licensed under the MIT license, users should verify the stability and security of the tool before integrating it into production environments.
