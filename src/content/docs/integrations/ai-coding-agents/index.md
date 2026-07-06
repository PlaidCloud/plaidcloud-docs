---
title: AI Agents (MCP)
description: Connect Claude, Cursor, GitHub Copilot, Gemini, and other AI agents to your PlaidCloud tenant through the Model Context Protocol (MCP) server.
sidebar:
  label: AI Agents (MCP)
  order: 13
---

PlaidCloud exposes a curated [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server at `/mcp` on every workspace. AI agents connect to it the same way they connect to any other MCP server, then call the tools to read projects, run workflows, query tables, manage dimensions, and more.

The pages in this section cover what the server exposes, how to authenticate, and step-by-step setup for the most common AI clients.

## What Makes PlaidCloud's AI Analysis Different

- **[Answers You Can Trust](./honest-answers/)** — every answer carries a confidence signal and plain-language caveats, and PlaidCloud never invents a number. This honesty is what lets you act on an AI answer without re-checking it by hand.
- **[Tracing Allocations](./tracing-allocations/)** — ask *why* an allocated result changed, what feeds it, and what a hypothetical change would do — in plain language.
- **[Analysis Paths](./analysis-paths/)** — give your key tables friendly names and a default, so you can just ask "why did this go up last quarter?"

## Connect Your Assistant

- [Getting Started](./getting-started/) — what the MCP server exposes and how to authenticate.
- [Microsoft 365 Copilot](/integrations/microsoft-365-copilot/) — bring PlaidCloud to your whole team in Teams and Outlook.
- Per-client setup: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/).
