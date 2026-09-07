---
title: anthropics/fermats-last-theorem
source: https://github.com/anthropics/fermats-last-theorem
stars: 889
category: Languages & Runtimes
---

# anthropics/fermats-last-theorem

- **URL**: https://github.com/anthropics/fermats-last-theorem
- **Stars**: 889
- **Language**: Lean
- **Category**: Languages & Runtimes
- **Topics**: None

## What it does
This repository provides a complete, machine-checked proof of Fermat's Last Theorem using Lean 4, specifically built on Mathlib. It includes a detailed verification process and a web-based presentation of the proof.

## Why it's interesting
The project stands out due to its rigorous verification of a historically significant mathematical theorem, ensuring that the proof is both machine-checked and relies solely on Lean's standard axioms. This level of verification is not commonly found in mathematical proofs, making it a unique contribution to both the Lean community and mathematical literature.

## How it works
The proof is structured in Lean 4, with the main theorem declared in `Theorems/Thm_fermat_last_theorem.lean`. The verification process involves building the entire repository with Lean's kernel and using tools like `comparator` and `nanoda` to ensure the proof's integrity. The repository also includes a detailed `PROOF-PATH.md` that outlines each step of the proof and its corresponding Lean theorem. However, the README does not specify how the Lean code is organized beyond the mentioned directories, leaving some uncertainty about the overall architecture.

## Get started in 5 minutes
To try it, clone the repository and run the following commands:
```sh
git clone https://github.com/anthropics/fermats-last-theorem flt && cd flt
LEAN_NUM_THREADS=96 lake build
```
This requires Lean 4.33.1 and Mathlib to be built from source, as detailed in the README.

## Watch out for
The repository is marked as a research artifact, not maintained, and not accepting contributions. It requires significant system resources for building and verification, including up to 300 GB of memory and 67 GB of disk space. Additionally, it is licensed under the Apache License 2.0, and users should be aware of the dependencies on external projects and the potential for deprecation warnings during the build process.
