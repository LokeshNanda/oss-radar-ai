---
title: bashalarmistalt/decimen-optical-transfer
source: https://github.com/bashalarmistalt/decimen-optical-transfer
stars: 3772
category: Web & Frontend
---

# bashalarmistalt/decimen-optical-transfer

- **URL**: https://github.com/bashalarmistalt/decimen-optical-transfer
- **Stars**: 3772
- **Language**: TypeScript
- **Category**: Web & Frontend
- **Topics**: None

## What it does
Decimen Optical Transfer allows users to send files between two devices using only a screen and a camera, by displaying animated QR codes that encode the file data. It supports file sizes up to 64 MB and can also transmit text snippets, all without requiring a network connection or app installation.

## Why it's interesting
This project stands out due to its use of fountain coding, which allows for robust data transfer even in the presence of frame loss, making it more efficient than traditional methods that rely on direct transmission. It also operates entirely offline after the initial visit, which is uncommon for file transfer solutions.

## How it works
The sender generates a continuous stream of QR codes, each representing a pseudorandom subset of the file's data blocks, allowing the receiver to reconstruct the file from any combination of frames received. The implementation uses WebAssembly for decoding and requires secure contexts (HTTPS) to access camera features. The README does not specify the exact libraries used for the QR code generation beyond mentioning `node-qrcode` and `zxing-wasm`, leaving some uncertainty about the complete architecture.

## Get started in 5 minutes
1. Clone the repository and navigate to the directory.
2. Run `npm install` to install dependencies.
3. Start the development server with `npm run dev`.
4. Open `https://localhost:5173/send/` on the sending device and `https://<lan-ip>:5173/receive/` on the receiving device.
5. Follow the on-screen instructions to send a file or text snippet.

## Watch out for
The project is a proof of concept and may not be fully mature for production use. There are caveats regarding camera permissions on mobile devices when using local files, as iOS Safari and Android Chrome may not allow camera access from `file://` URLs. Additionally, the README notes that the transfer is not encrypted, meaning that any data displayed on the sender's screen is visible to anyone with a camera pointed at it.
