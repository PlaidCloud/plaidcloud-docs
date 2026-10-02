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

* **LLM Connection** *(required)* — a connection of kind LLM (for example, Anthropic). Its **Agent Access** must be **Read & write** for any Write binding. **Full** also allows writes until it is removed on January 15, 2027, and a step that uses it logs a warning when it completes. At **Read & write** a step writes only to bindings with Write checked, and cannot run SQL that writes or create tables.
* **Model** *(optional)* — defaults to the connection's default model. Any Claude model works with an Anthropic connection, older models such as Claude Sonnet 4.5 included.
* **Prompt** *(required)* — supports `{{tables.NAME}}`, `{{dimensions.NAME}}`, and `{{documents.NAME}}` references to bound objects.
* **Result schema** *(optional for Anthropic; required for other providers)* — a JSON Schema (root `"type": "object"`) for a captured structured summary; with Anthropic, leave blank when the model's work is its MCP writes. Non-Anthropic providers have no MCP access, so a schema is required.
* **Bindings** — Tables, Dimensions, and Documents the model may access, each picked with a selector and granted **Read** and/or **Write**. Write tables receive inserted rows, write dimensions receive nodes, write documents receive uploaded files.
* **Limits** — Max output tokens (1,024 to 128,000) and Credential TTL (60 to 3,600 seconds).

## Behavior

* The model call runs in its own job. A short-lived, scoped credential is minted for the run and revoked when it ends.
* Access is gated per object and per checkbox: the model reads only Read-bound objects and writes only Write-bound ones — never an object you didn't bind. Writing requires an existing destination object; the step doesn't create one.
* Each run makes a billable provider call and writes into your bound objects.

## What's Checked When You Save

* **Result schema** — when you provide one, it must be valid JSON, a JSON object, and declare `"type": "object"` at its root. Otherwise saving is refused, for example with *The result schema must declare "type": "object" at its root.*
* **Bindings and the connection** — only an Anthropic connection gives the model access to bindings. Saving a step with bindings on another provider's connection is refused, with a message naming the provider and asking you to *Remove the bindings or choose an Anthropic connection.* A binding with **Write** checked needs a connection whose **Agent Access** allows writes. On a Read-only connection, saving is refused with *The selected LLM connection has Read-only Agent Access, so a binding with Write checked could not write. Set the connection to 'Read & write' or uncheck Write on the bindings.* A step saved through the API with no connection is checked against the workspace's default LLM connection, which it also runs on: the one an admin marked as the default, or else the most recently updated. Without an admin-marked default, editing another LLM connection makes that one the default, and can refuse the step's next save.
