---
title: ikow/php2shell-poc
source: https://github.com/ikow/php2shell-poc
stars: 1818
category: Security
---

# ikow/php2shell-poc

- **URL**: https://github.com/ikow/php2shell-poc
- **Stars**: 1818
- **Language**: Python
- **Category**: Security
- **Topics**: cve-2026-109618, cve-2026-109619, detection-rules, exploit, php-exploit, php-security, php2shell, poc, rce, session-upload-progress, suricata-rules, vulnerability-research, waf-rules, wordpress-security

## What it does
This repository provides a proof of concept (PoC) for exploiting two critical vulnerabilities in PHP (CVE-2026-109618 and CVE-2026-109619) that allow for remote code execution (RCE) via PHP's `session.upload_progress`. It includes five independent RCE chains and detection rules for various security tools like Suricata and ModSecurity.

## Why it's interesting
Unlike typical exploit repositories, this project not only demonstrates the vulnerabilities but also provides a comprehensive toolkit for detection and mitigation. It impacts a significant portion of PHP applications, including popular CMS platforms like WordPress and Joomla, making it highly relevant for developers and security professionals.

## How it works
The repository contains multiple exploit scripts that leverage different attack vectors, such as session injection and use-after-free (UAF) vulnerabilities. It also includes detection rules for various security systems to help identify attempts to exploit these vulnerabilities. The architecture is organized into directories for exploits, detection rules, and proof of concept verification scripts, with a lab setup using Docker for testing.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/ikow/php2shell-poc.git`
2. Navigate to the lab directory: `cd php2shell-poc/lab`
3. Start the Docker environment: `docker compose up -d`
4. Verify an exploit chain: `python3 ../poc/verify_session_injection.py --target http://127.0.0.1:18080`

## Watch out for
The repository is relatively new, created in October 2026, and may not have extensive community support yet. The exploit code for the most critical chains (D and E) is available only to paid subscribers, which may limit access for some users. Additionally, the repository is intended for authorized security testing and educational purposes only, emphasizing the need for ethical use.
