---
title: feder-cr/git-ai
source: https://github.com/feder-cr/git-ai
stars: 2367
category: Developer Tools
---

# feder-cr/git-ai

- **URL**: https://github.com/feder-cr/git-ai
- **Stars**: 2367
- **Language**: Go
- **Category**: Developer Tools
- **Topics**: ai-agents, coding-agents, git, golang, scion, version-control

## What it does
`git-ai` (also known as `gitai`) is an open-source version control system designed specifically for AI agents. It allows multiple agents to read, write, and land code concurrently, optimizing the process for rapid, short-lived tasks rather than traditional long-lived human workflows.

## Why it's interesting
Unlike classic Git, which is built for human users who clone repositories and push changes after long periods, `gitai` is server-centric and designed to handle thousands of quick tasks efficiently. It implements concepts from Anthropic's internal Scion system, allowing for features like automatic conflict resolution and a changeset log that tracks every update in real-time.

## How it works
`gitai` operates with always-online clients that fetch only necessary data, while history queries are processed server-side. It uses a compare-and-swap mechanism for landing changes, which allows for concurrent updates without a merge queue. The architecture includes a server that manages changesets, object storage, and a database (SQLite or PostgreSQL) for state management. The README mentions various components like `graft-cache`, `graft CLI`, and `graft` configuration, but details on specific implementation or performance metrics beyond benchmarks are not fully elaborated.

## Get started in 5 minutes
To quickly set up `gitai`, clone the repository and build the project:
```shell
git clone https://github.com/feder-cr/git-ai.git
cd git-ai
make build                         # server, CLI and tools into _build/bin
examples/graft/quickstart.sh       # sets up a server and agents
./_build/bin/graft                 # runs the CLI
```

## Watch out for
The project is currently at version 0.2.0, indicating it may still be in development with potential interface changes before reaching 1.0. Known limitations, such as garbage collection of packs in the storage core, are documented in `LIMITATIONS.md`. Additionally, while it is MIT licensed, developers should be aware of its origins as a fork of Gitaly, which may have implications for compatibility and support.
