---
title: duty1g/x64dbg-mcp-server
source: https://github.com/duty1g/x64dbg-mcp-server
stars: 1142
category: Developer Tools
---

# duty1g/x64dbg-mcp-server

- **URL**: https://github.com/duty1g/x64dbg-mcp-server
- **Stars**: 1142
- **Language**: Zig
- **Category**: Developer Tools
- **Topics**: ai-agents, ai-debugging, binary-analysis, claude, claude-code, malware-analysis, malware-research, malware-scanner, mcp, mcp-server, mcp-servers, x64dbg, x64dbg-mcp, x64dbg-plugin, x64dbg-tools, xdbg, zig, zig-lang, ziglang

## What it does
The x64dbg-MCP Server is a plugin for the x64dbg debugger that implements the Model Context Protocol (MCP) to expose debugger functionalities over HTTP. It allows users to programmatically control x64dbg, enabling operations like setting breakpoints, reading memory, and managing execution flow using any MCP-compatible AI assistant.

## Why it's interesting
This plugin stands out due to its native implementation in Zig, which ensures zero dependencies and a single-binary output. It supports both x32 and x64 architectures from a single codebase and offers dual transport options (HTTP and SSE), making it versatile for various client setups. The automatic token-based authentication enhances security for remote debugging sessions.

## How it works
The plugin integrates with x64dbg by loading at startup and resolving necessary API symbols at runtime. It runs an HTTP server on a background thread, allowing MCP clients to send JSON-RPC requests that map directly to x64dbg SDK calls. The README does not specify how the plugin handles error states or performance under load, which leaves some uncertainty regarding its robustness in high-demand scenarios.

## Get started in 5 minutes
1. Download the latest release or build from source using Zig.
2. Copy the contents of the `dist/` directory into your x64dbg root folder.
3. Launch x64dbg; the MCP server will start automatically on default ports 9094 (x64) and 9095 (x32).
4. Configure your MCP client to connect to the server using the provided JSON configuration examples.

## Watch out for
The plugin is intended for legitimate use in reverse engineering and malware analysis, and it emphasizes the need for proper authorization before use. It communicates over unencrypted HTTP, which poses security risks if exposed to untrusted networks. The README also notes that the author disclaims liability for misuse, highlighting the importance of responsible usage.
