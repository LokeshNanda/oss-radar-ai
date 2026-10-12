---
title: LosaLosSantos/aurelio-finance
source: https://github.com/LosaLosSantos/aurelio-finance
stars: 2690
category: AI & Agents
---

# LosaLosSantos/aurelio-finance

- **URL**: https://github.com/LosaLosSantos/aurelio-finance
- **Stars**: 2690
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: ai, dividends, etf, finance, financial-planning, fintech, investing, llm, net-worth, personal-finance, portfolio-tracker, self-hosted, stocks, wealth-management

## What it does
Aurelio is a personal finance application that allows users to track their net worth, investments, and debts on their own computer. It features an optional AI advisor that can analyze financial data and provide insights based on user records.

## Why it's interesting
Unlike many personal finance apps that require cloud storage, Aurelio keeps all user data locally, enhancing privacy. The integration of an AI advisor that can interact with user data and provide tailored financial advice sets it apart from traditional finance tracking tools.

## How it works
The application is built using Python and requires Git, Node.js, and a specific package called `uv`. It operates by storing user data in a local SQLite database (`backend/data.db`) and can be run in demo mode or with personal data. The AI functionality relies on an external service (OpenRouter) for processing, requiring users to set up an API key. The README does not provide detailed architecture or dependencies beyond these components, leaving some uncertainty about the overall design.

## Get started in 5 minutes
1. Install Git, Node.js (22 or later), and `uv`.
2. Clone the repository: `git clone https://github.com/LosaLosSantos/aurelio-finance.git`
3. Navigate to the directory: `cd aurelio-finance`
4. Run the demo with `./start.sh --demo` (macOS/Linux) or `./start.ps1 -Demo` (Windows).
5. Access the app at <http://localhost:8000>.

## Watch out for
The project is relatively new (created in October 2026), so it may lack maturity and extensive community support. Users should be cautious about the AI costs associated with using OpenRouter, as detailed pricing is provided but may vary. The app is licensed under MIT, which is permissive but does not offer warranties or guarantees.
