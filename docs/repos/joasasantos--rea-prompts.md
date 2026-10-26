---
title: JoasASantos/REA-Prompts
source: https://github.com/JoasASantos/REA-Prompts
stars: 2601
category: Developer Tools
---

# JoasASantos/REA-Prompts

- **URL**: https://github.com/JoasASantos/REA-Prompts
- **Stars**: 2601
- **Language**: Batchfile
- **Category**: Developer Tools
- **Topics**: prompt-engineering, rea, reverse-enginnering

## What it does
REA-Prompts provides a collection of prompts designed for use with the REA (Reverse Engineer Anything) toolset, enabling users to analyze software, including binaries, firmware, and applications, by asking targeted questions.

## Why it's interesting
This repository stands out due to its focus on prompt engineering specifically tailored for reverse engineering tasks, allowing developers to leverage AI coding agents effectively. The prompts are structured to yield evidence-backed answers, which is crucial for accurate analysis in reverse engineering.

## How it works
The repository includes a setup script (`setup.sh` for macOS/Linux and `setup.bat` for Windows) that installs various skill packs into the user's coding agent's skills folder. Each skill pack contains a `SKILL.md` file with YAML frontmatter for auto-loading relevant prompts. The prompts cover a wide range of reverse engineering tasks, from feature tracing to malware analysis, and are organized into sections for easy navigation. The README also emphasizes responsible usage, particularly regarding legal and ethical considerations in reverse engineering.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/JoasASantos/REA-Prompts`
2. Navigate to the directory: `cd REA-Prompts`
3. Run the setup script for your OS: `./setup.sh` (macOS/Linux) or `setup.bat` (Windows).
4. Use the prompts directly in your REA agent by replacing placeholders in the examples provided in the README.

## Watch out for
The repository is relatively new (created in October 2026), so it may lack extensive documentation or community support. Users should also be cautious about the ethical implications of using the prompts, as the README warns against using them for unauthorized software analysis.
