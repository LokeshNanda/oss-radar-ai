---
title: awesome-dsh-plugin/awesome-dsh-plugin
source: https://github.com/awesome-dsh-plugin/awesome-dsh-plugin
stars: 7938
category: Developer Tools
---

# awesome-dsh-plugin/awesome-dsh-plugin

- **URL**: https://github.com/awesome-dsh-plugin/awesome-dsh-plugin
- **Stars**: 7938
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: awesome, awesome-list, deepseek-harness, dsh, dsh-plugin

## What it does
This repository provides a curated list of plugins for the DeepSeek Harness (dsh), an open-source coding agent framework. The plugins can be installed via the command `dsh plugin add` and are designed to extend the functionality of the DeepSeek Harness by allowing users to customize and enhance their coding experience.

## Why it's interesting
Unlike typical plugin repositories, this list emphasizes community contributions and maintains a strict review process for submissions, ensuring that each plugin meets specific criteria for functionality and maintenance. This focus on curation helps users find reliable plugins without needing to sift through unverified options.

## How it works
The repository collects plugins that declare a `dsh.bundle` manifest, which allows them to be installed through the DeepSeek Harness. Each plugin is checked against its source for compliance with the repository's submission criteria, which include proper installation and functionality as described. However, the README does not provide detailed information on the underlying architecture of the DeepSeek Harness itself, leaving some uncertainty about how plugins interact with the core system.

## Get started in 5 minutes
To try it out, first install the DeepSeek Harness from its [GitHub repository](https://github.com/deepseek-ai/deepseek-harness). Then, use the command `dsh plugin add <plugin-name>` to install any plugin from the list provided in this repository. For example, to install the dsh-market plugin, run:
```sh
dsh plugin add dshmarket
```

## Watch out for
While the repository has a significant number of stars (7938), it was created recently in August 2026, which may indicate that it is still evolving. Users should be cautious about security, as installing plugins runs third-party code with user permissions, and the repository does not conduct security reviews of the plugins. It is advisable to check the source of any plugin before installation.
