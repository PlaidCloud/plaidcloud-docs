---
title: LLM Step
description: Run a prompt against an LLM with scoped read-only access to project data, returning a schema-validated JSON response routed to outputs such as generated PDFs.
sidebar:
  order: 5
---

## Description

The **LLM Step** sends a prompt to a large language model and routes its structured response to outputs. With an Anthropic LLM connection, the model gets scoped, read-only access to the project tables, dimensions, and documents you bind; the response must match a JSON Schema you supply.

For a full walkthrough, see the [LLM Step guide](/guides/workflows/llm-step/).

## Configuration

* **LLM Connection** *(required)* — a connection of kind LLM (for example, Anthropic).
* **Model** *(optional)* — defaults to the connection's default model.
* **Prompt** *(required)* — supports `{{tables.NAME}}`, `{{dimensions.NAME}}`, and `{{documents.NAME}}` references to bound objects.
* **Result schema** *(required)* — a JSON Schema (root `"type": "object"`) the response must match.
* **Bindings** — read-only Tables, Dimensions, and Documents the model may access.
* **Outputs** *(at least one)* — currently `pdf_per_item`: one PDF per item of an array field, rendered from a Markdown field and uploaded to a document account.
* **Limits** — Max output tokens (1,024 to 128,000) and Credential TTL (60 to 3,600 seconds).

## Behavior

* The model call runs in its own job; access is read-only and limited to the bound objects.
* Each run makes a billable provider call and writes its outputs.
