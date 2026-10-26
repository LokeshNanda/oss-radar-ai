---
title: EthanArbuckle/fairplay-decrypt
source: https://github.com/EthanArbuckle/fairplay-decrypt
stars: 2152
category: Security
---

# EthanArbuckle/fairplay-decrypt

- **URL**: https://github.com/EthanArbuckle/fairplay-decrypt
- **Stars**: 2152
- **Language**: C
- **Category**: Security
- **Topics**: None

## What it does
This repository provides a tool for decrypting FairPlay-encrypted iOS applications (IPAs) using a 16-byte credential associated with the account that owns each IPA. It supports decryption on macOS and Linux and can handle specific versions of SUPF and SINF records.

## Why it's interesting
Unlike other decryption tools, this one allows for independent key derivation from the credentials, which may offer more flexibility in handling different types of encrypted content. It also focuses on offline decryption, which can be advantageous for users who prefer not to rely on online services.

## How it works
The tool uses Python to derive page keys from the IPA's SINF and SUPF records, decrypting the encrypted arm64 Mach-O slices and clearing the `cryptid`. The README specifies that the decryption process requires a `credential.bin` file, which can be obtained from a supported jailbroken device. The setup involves creating a Python virtual environment and installing dependencies listed in `requirements.txt`. However, the README does not provide details on the specific algorithms or methods used for key derivation, leaving some uncertainty about the implementation specifics.

## Get started in 5 minutes
1. Clone the repository.
2. Create a Python virtual environment: `python3 -m venv .venv`
3. Activate the virtual environment: `. .venv/bin/activate`
4. Install dependencies: `python -m pip install -r requirements.txt`
5. Run the decryption command: `python decrypt.py /path/to/encrypted.ipa /path/to/decrypted.ipa --credential /path/to/credential.bin`.

## Watch out for
The repository does not specify a license, which could lead to legal concerns regarding usage. Additionally, the tool is designed for jailbroken devices, which may pose security risks. The README lacks information on the maturity of the project, potential bugs, or limitations in supported IPA formats, which could affect usability.
