---
title: guillaumemeyer/watermarks-remover
source: https://github.com/guillaumemeyer/watermarks-remover
stars: 13739
category: Developer Tools
---

# guillaumemeyer/watermarks-remover

- **URL**: https://github.com/guillaumemeyer/watermarks-remover
- **Stars**: 13739
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: agent-skill, ai, c2pa, claude, provenance, synthid, watermark

## What it does
This repository provides a Python-based service and skill for stripping AI provenance marks from various file types, including PNG, JPEG, SVG, PDF, DOCX, and HTML. It focuses on removing invisible Unicode characters, statistical text watermarks, and metadata from files to ensure content privacy and hygiene.

## Why it's interesting
Unlike many watermark removal tools that focus on specific vendors or file types, this tool supports a wide range of formats and employs a modular architecture that allows for easy integration with other systems via HTTP. Its ability to handle multiple AI watermarking schemes makes it versatile for developers working with AI-generated content.

## How it works
The tool is structured into layers: Layer A targets invisible Unicode and exotic characters using deterministic scripts, while Layer B addresses statistical text watermarks through an agent rewrite mechanism. The service operates over HTTP, allowing external applications to interact with it without needing to embed Python code. It includes various scripts for inspecting and cleaning files, and it can be run locally or via Docker. The HTTP service exposes endpoints for health checks, capabilities, and file processing, with support for optional external tools like `exiftool` and `c2patool` for enhanced functionality.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/guillaumemeyer/watermarks-remover`
2. Navigate to the project directory.
3. Start the local HTTP server using: `python3 service/scripts/server.py --host 127.0.0.1 --port 8765`
4. Use the provided scripts to inspect or clean files, e.g., `python3 service/scripts/clean_file.py draft.md -o draft.cleaned.md`.

## Watch out for
The repository is relatively new, created in August 2026, and while it has gained significant attention with over 13,000 stars, the maturity of the tool and its long-term support are uncertain. Additionally, the README does not specify licensing details, which is crucial for developers considering its use in commercial applications.
