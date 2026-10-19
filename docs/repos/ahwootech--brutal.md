---
title: ahwootech/BRUTAL
source: https://github.com/ahwootech/BRUTAL
stars: 1941
category: Developer Tools
---

# ahwootech/BRUTAL

- **URL**: https://github.com/ahwootech/BRUTAL
- **Stars**: 1941
- **Language**: C#
- **Category**: Developer Tools
- **Topics**: csharp, dotnet, game-engine, gamedev, vulkan

## What it does
BRUTAL is a C# framework designed for game development, allowing developers to create games or build their own game engines. It provides direct access to native APIs and Vulkan, along with low-level libraries for various functionalities such as memory management, concurrency, and logging.

## Why it's interesting
BRUTAL differentiates itself from mainstream game engines like Unity and Unreal by offering a deliberately minimalistic approach, focusing on low-level control and performance without the overhead of a full-fledged game engine. It allows developers to build their own systems on top of its core functionalities, promoting independence from proprietary tools.

## How it works
BRUTAL consists of multiple libraries, each published as a NuGet package, covering aspects like interop, memory management, and Vulkan bindings. The framework does not impose architectural decisions, allowing developers to choose their stack and integrate third-party NuGet packages as needed. However, it lacks a built-in editor, scene graph, or renderer, which may require additional development effort for those features.

## Get started in 5 minutes
1. Install the [.NET 10 SDK](https://dotnet.microsoft.com/download) and ensure you have a Vulkan-capable GPU.
2. Create a new console project:
   ```sh
   dotnet new console -n HelloBrutal
   cd HelloBrutal
   dotnet add package Ahwoo.Brutal.Core
   dotnet add package Ahwoo.Brutal.Glfw
   ```
3. Replace `Program.cs` with the provided example code to create a window and run the application.
4. Execute the project with `dotnet run`.

## Watch out for
BRUTAL is relatively new, having been created in October 2026, which may affect its maturity and community support. The README emphasizes that it is not a general-purpose engine and lacks certain features that are standard in other engines, which could be a limitation for developers expecting a more comprehensive toolset. Additionally, while the framework is open source under an MIT-based license, it requires attribution in commercial products, which may not suit all developers.
