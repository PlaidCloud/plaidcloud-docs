---
title: INITCAP (Lakehouse v2)
description: INITCAP — Schreibt den ersten Buchstaben jedes Worts in einer Zeichenfolge groß.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

Schreibt den ersten Buchstaben jedes Worts in einer Zeichenfolge groß.

## Analyze-Syntax

```python
func.initcap(<str>)
```

## Analyze-Beispiele

```python
func.initcap('hello world')

┌───────────────┐
│ 'Hello World'  │
└───────────────┘
```

## SQL-Syntax

```sql
INITCAP(<str>)
```

## SQL-Beispiele

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
