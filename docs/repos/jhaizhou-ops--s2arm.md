---
title: jhaizhou-ops/S2Arm
source: https://github.com/jhaizhou-ops/S2Arm
stars: 1433
category: Other
---

# jhaizhou-ops/S2Arm

- **URL**: https://github.com/jhaizhou-ops/S2Arm
- **Stars**: 1433
- **Language**: C#
- **Category**: Other
- **Topics**: apple-silicon, arm64, game-porting, ios, ipados, macos, metal, s2arm, static-recompilation, switch

## What it does
S2Arm allows users to run Nintendo Switch games natively on iPhone, iPad, and Mac by rewriting game code to ARM64 and using Metal for graphics. It provides a single app interface for managing multiple games, enabling users to import their own game files and keys for play.

## Why it's interesting
Unlike traditional emulators, S2Arm does not use CPU emulation, which can lead to performance issues. Instead, it directly compiles and runs the game code on compatible Apple devices, promising better speed and efficiency. The integration of AI for game management and diagnostics further distinguishes it from other game porting solutions.

## How it works
S2Arm operates by rewriting the ARM64 code of Switch games at build time, allowing them to run directly on the device's processor. It uses a graphical launcher for both Mac and Windows, simplifying the import and build process. The README mentions a control interface (`s2armctl`) that facilitates AI-driven game management, but specific implementation details about the AI's capabilities are not fully outlined.

## Get started in 5 minutes
1. Download the launcher for Mac or Windows from the [download page](https://jhaizhou-ops.github.io/S2Arm/).
2. Open the launcher and follow the prompts to set up your environment, including installing Xcode if on Mac.
3. Import your game files and keys, select your target device, and click Build to start the process.

## Watch out for
S2Arm is still in development, with a noted limitation of only supporting 64-bit games, as 32-bit games cannot be executed on Apple silicon. Users must also provide their own game files legally, as the project does not ship any games or keys. Additionally, the AI features may not be fully fleshed out, and the README does not provide exhaustive details on potential issues or limitations in the AI's functionality.
