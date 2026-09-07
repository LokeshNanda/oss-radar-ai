---
title: sebbbi/NoGraphicsAPI
source: https://github.com/sebbbi/NoGraphicsAPI
stars: 1017
category: Developer Tools
---

# sebbbi/NoGraphicsAPI

- **URL**: https://github.com/sebbbi/NoGraphicsAPI
- **Stars**: 1017
- **Language**: C++
- **Category**: Developer Tools
- **Topics**: None

## What it does
`NoGraphicsAPI` is a minimal graphics API built on Vulkan 1.4 that simplifies the graphics programming model by using 64-bit GPU pointers and application-owned descriptor heaps. It aims to reduce the complexity of traditional graphics APIs by eliminating many conventional constructs such as buffer objects and descriptor sets.

## Why it's interesting
This project stands out by implementing a radically simplified API that closely aligns with the concepts presented in Sebastian Aaltonen's blog post and SIGGRAPH talk. It leverages the latest Vulkan extensions to provide a unique approach to graphics programming, focusing on direct memory management and execution hazards instead of resource states.

## How it works
The API operates by allowing applications to manage GPU memory and descriptor heaps directly, using GPU pointers for resource access. Key features include the use of `vkCmdPushDataEXT` for root data management, explicit asynchronous submission of command buffers, and a focus on global barriers for synchronization. However, it currently lacks support for Metal and has not implemented certain Vulkan features such as ray tracing and multi-threading.

## Get started in 5 minutes
To get started, ensure you have CMake 3.24+, a C++20 compiler, and Vulkan SDK version 1.4.357 or newer. Clone the repository, then run the following commands:
```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
cmake --install build --prefix path/to/install
```
This will build the `NoGraphicsAPI` library and its utility components.

## Watch out for
The repository is still experimental and lacks full support for all Vulkan features, including ray tracing and multi-threading. Additionally, it does not currently support Linux swap chain functionality, and driver support is limited to specific AMD and NVIDIA architectures. The project is licensed under the MIT License, which is permissive but requires attribution.
