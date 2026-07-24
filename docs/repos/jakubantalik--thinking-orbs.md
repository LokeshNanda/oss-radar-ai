---
title: Jakubantalik/thinking-orbs
source: https://github.com/Jakubantalik/thinking-orbs
stars: 905
category: Web & Frontend
---

# Jakubantalik/thinking-orbs

- **URL**: https://github.com/Jakubantalik/thinking-orbs
- **Stars**: 905
- **Language**: TypeScript
- **Category**: Web & Frontend
- **Topics**: None

## What it does
The `thinking-orbs` library provides animated loading indicators designed specifically for AI and agent user interfaces. It features six distinct animated states and two size options, all rendered on a 2D canvas without relying on WebGL or filters.

## Why it's interesting
Unlike typical loading indicators, `thinking-orbs` offers a unique set of animations that represent different states of an agent's activity, enhancing user experience in AI applications. Its automatic theme detection and performance optimizations, such as pausing animations when offscreen, make it suitable for modern web applications.

## How it works
The library uses a plain 2D canvas to render animations, ensuring compatibility across major browsers. It supports six states, each with a specific animation, and two sizes tailored for different UI contexts. The theme adapts automatically based on the host project's settings, utilizing `MutationObserver` and `prefers-color-scheme` for live updates. Accessibility features include appropriate ARIA roles and reduced motion options. However, the README does not specify how the animations are implemented or the underlying logic for the state transitions.

## Get started in 5 minutes
To use `thinking-orbs`, install it via npm with `npm install thinking-orbs`, then import and use the `ThinkingOrb` component in your React application as follows:
```tsx
import { ThinkingOrb } from 'thinking-orbs';

function Status() {
  return <ThinkingOrb state="searching" size={64} />;
}
```

## Watch out for
The repository has no topics tagged, which may affect discoverability. While it has garnered 905 stars, the README does not provide extensive documentation on customization or advanced usage. The library is licensed under MIT, which is permissive, but developers should ensure it meets their project's requirements before use.
