---
title: LLM Step
description: Run a prompt against an LLM with scoped read and/or write access to project data, where the model writes its results back directly through the MCP server.
sidebar:
  order: 5
---

## Description

The **LLM Step** sends a prompt to a large language model. With an Anthropic LLM connection, the model gets scoped access to the project tables, dimensions, and documents you bind — **Read**, **Write**, or both per object — and writes its results directly into the Write-enabled bindings. A Write binding is the step's output; there is no separate output format.

For a full walkthrough, see the [LLM Step guide](/guides/workflows/llm-step/).

## Configuration

* **LLM Connection** *(required)* — a connection of kind LLM (for example, Anthropic). Its **Agent Access** must be **Read & write** or **Full** for any Write binding.
* **Model** *(optional)* — defaults to the connection's default model.
* **Prompt** *(required)* — supports `{{tables.NAME}}`, `{{dimensions.NAME}}`, and `{{documents.NAME}}` references to bound objects.
* **Result schema** *(optional for Anthropic; required for other providers)* — a JSON Schema (root `"type": "object"`) for a captured structured summary; with Anthropic, leave blank when the model's work is its MCP writes. Non-Anthropic providers have no MCP access, so a schema is required.
* **Bindings** — Tables, Dimensions, and Documents the model may access, each picked with a selector and granted **Read** and/or **Write**. Write tables receive inserted rows, write dimensions receive nodes, write documents receive uploaded files.
* **Limits** — Max output tokens (1,024 to 128,000) and Credential TTL (60 to 3,600 seconds).

## Behavior

* The model call runs in its own job. A short-lived, scoped credential is minted for the run and revoked when it ends.
* Access is gated per object and per checkbox: the model reads only Read-bound objects and writes only Write-bound ones — never an object you didn't bind. Writing requires an existing destination object; the step doesn't create one.
* Each run makes a billable provider call and writes into your bound objects.
