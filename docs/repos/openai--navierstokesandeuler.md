---
title: openai/NavierStokesAndEuler
source: https://github.com/openai/NavierStokesAndEuler
stars: 1872
category: Languages & Runtimes
---

# openai/NavierStokesAndEuler

- **URL**: https://github.com/openai/NavierStokesAndEuler
- **Stars**: 1872
- **Language**: Lean
- **Category**: Languages & Runtimes
- **Topics**: None

## What it does
This repository contains formalizations in Lean 4 for results related to finite time blowup in the Navier-Stokes and Euler equations. It provides proofs for specific scenarios where global smooth solutions do not exist under certain conditions.

## Why it's interesting
The repository formalizes significant mathematical results that are part of the Millennium Prize Problems, specifically addressing the existence and smoothness of solutions to the Navier-Stokes equations. This formalization in Lean 4 allows for rigorous proof checking, which is not commonly found in traditional mathematical literature.

## How it works
The project is built using Lean 4.34.0-rc2, Mathlib, and Lake. It includes proofs for both the Navier-Stokes and Euler equations, detailing conditions under which solutions develop singularities. The README provides instructions for building the formalizations and checking proofs using Comparator, although specific details about the architecture or internal structure of the Lean formalizations are not provided.

## Get started in 5 minutes
To get started, install elan, fetch the mathlib cache, and build the formalizations with the following commands:
```sh
lake exe cache get
lake build
```

## Watch out for
The repository is relatively new, created in September 2026, and may not have extensive documentation or community support yet. Users should be aware of potential gaps in the README regarding detailed usage instructions and examples. Additionally, the repository does not specify a license, which may affect usage rights.
