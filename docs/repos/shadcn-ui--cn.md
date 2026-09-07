---
title: shadcn-ui/cn
source: https://github.com/shadcn-ui/cn
stars: 1231
category: Developer Tools
---

# shadcn-ui/cn

- **URL**: https://github.com/shadcn-ui/cn
- **Stars**: 1231
- **Language**: TypeScript
- **Category**: Developer Tools
- **Topics**: clsx, cn, shadcn, tailwind-merge, tailwindcss

## What it does
`cn` is a TypeScript library designed for merging Tailwind CSS classes and resolving conflicts. It serves as a drop-in replacement for `tailwind-merge` and `clsx`, claiming to be significantly faster while maintaining the same API.

## Why it's interesting
`cn` claims to be 30× faster than the combined performance of `clsx` and `tailwind-merge`, which is a notable improvement for developers working with Tailwind CSS. It has zero dependencies and is framework-agnostic, making it versatile across various JavaScript frameworks and environments.

## How it works
The library uses a caching mechanism to optimize repeated calls, which allows it to skip redundant processing. It maintains compatibility with existing APIs from `tailwind-merge` and `clsx`, ensuring a smooth transition for users. The README provides benchmarks comparing `cn` against its predecessors, showing significant performance gains in various scenarios. However, the exact internal architecture and optimization strategies are not detailed, leaving some uncertainty about its implementation.

## Get started in 5 minutes
To install `cn`, run:
```bash
npm i cn
```
Then, you can use it in your project by importing it and replacing existing imports from `clsx` and `tailwind-merge` as shown in the README. For migration, you can use:
```bash
npx shadcn@latest migrate cn
```

## Watch out for
The library is relatively new, created in August 2026, which may imply limited community support or maturity. It supports Tailwind CSS v4 but not v3, and classes that resemble Tailwind utilities are treated as such, which could lead to unexpected behavior. Additionally, the CLI requires Node 20+, and there are specific guidelines for dynamically constructed class names that may require attention.
