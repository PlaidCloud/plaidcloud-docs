---
title: AI Agents (MCP)
description: Connect Claude, Cursor, GitHub Copilot, Gemini, and other AI agents to your PlaidCloud tenant through the Model Context Protocol (MCP) server.
sidebar:
  label: AI Agents (MCP)
  order: 13
---

PlaidCloud exposes a curated [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server at `/mcp/` on every workspace. AI agents connect to it the same way they connect to any other MCP server, then call the tools to read projects, run workflows, query tables, manage dimensions, and more.

The pages in this section cover what the server exposes, how to authenticate, and step-by-step setup for the most common AI clients.
