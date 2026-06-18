---
title: Prettify (Format) Code in Editors
description: Use the Prettify button or Shift+Alt+F to auto-format SQL, JSON, and expression code in PlaidCloud workflow step editors.
sidebar:
  order: 12
---

## Prettify Code in Editors

Several workflow step editors use a code editor — the SQL steps (Frame Extract SQL, Remote Execute SQL, Remote Direct SQL, Remote Export SQL, and Import SQL), the LLM step's **Result schema** (JSON), and the Expression Editor used throughout the flow areas.

Each of these editors has a **Prettify** button that reformats the code in place — indenting it and laying it out consistently so it is easier to read and review. You can also press **Shift+Alt+F** (**Shift+Option+F** on macOS) while the cursor is in the editor.

## What Gets Formatted

- **SQL** — reformatted into a readable, multi-line layout: one clause per line, aligned `CASE` / `WHEN`, and broken-out nested functions. Project variables and template tokens such as `{variable}`, `{{ ... }}`, and `{% ... %}` are preserved exactly.
- **JSON** — re-indented with two-space indentation (for example, the LLM step's Result schema).
- **Expressions** — PlaidCloud expressions are formatted with standard Python formatting: consistent spacing around operators and commas, and line breaks for long expressions.

## Things to Know

- Prettify never changes what your code does — only how it is laid out. SQL keywords and identifiers keep their original casing.
- If the code cannot be parsed (a syntax error), Prettify leaves it untouched and shows a brief message, so you never lose your work.
- Formatting applies as a single step — press **Ctrl+Z** (**Cmd+Z** on macOS) to undo it.
