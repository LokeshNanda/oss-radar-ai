---
title: dmmulroy/anti-slop
source: https://github.com/dmmulroy/anti-slop
stars: 2435
category: Developer Tools
---

# dmmulroy/anti-slop

- **URL**: https://github.com/dmmulroy/anti-slop
- **Stars**: 2435
- **Language**: TypeScript
- **Category**: Developer Tools
- **Topics**: agent-skills, linting, oxlint, typescript

## What it does
The `anti-slop` repository provides a set of opinionated linting rules for TypeScript and JavaScript, specifically designed to reject low-evidence coding patterns. It is intended to be integrated into projects as a vendored solution rather than a fixed npm dependency.

## Why it's interesting
Unlike standard linting tools, `anti-slop` focuses on enforcing stricter type safety and evidence-based coding practices, which can help teams maintain high code quality and reduce runtime errors. Its rules are tailored to address common pitfalls in TypeScript and JavaScript development, making it a specialized tool for developers who prioritize type safety.

## How it works
The repository includes a set of linting rules that can be integrated into a project using an agent skill or through manual installation. The rules are defined in a configuration file (`oxlint.config.ts`), and the README provides detailed examples of code patterns that each rule rejects. The installation process involves copying the source files into the target repository and configuring the linting setup accordingly. However, the README does not specify how the rules are implemented internally or how they interact with the Oxlint framework beyond the configuration.

## Get started in 5 minutes
1. Run the command to add the skill: `npx skills add dmmulroy/anti-slop --skill install-anti-slop`.
2. Ask your coding agent to install or configure `anti-slop` in your current repository.
3. Alternatively, manually copy the `src/` directory into your project and configure `oxlint.config.ts` as described in the README.

## Watch out for
The repository is relatively new, created in August 2026, which may imply limited community support or maturity. Additionally, it is licensed under MIT, which is permissive, but users should ensure compliance with any dependencies. There is no mention of ongoing maintenance or updates, so users should be cautious about potential gaps in support or documentation.
