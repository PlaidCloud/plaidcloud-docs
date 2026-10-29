---
title: REPLACE (Lakehouse v2)
description: REPLACE — Ersetzt alle Vorkommen einer Teilzeichenfolge durch eine andere Teilzeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/replace.md
---

Ersetzt alle Vorkommen einer Teilzeichenfolge durch eine andere Teilzeichenfolge.

## Analyze-Syntax

```python
func.replace(<str>, <old>, <new>)
```

## Analyze-Beispiele

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## SQL-Syntax

```sql
REPLACE(<str>, <old>, <new>)
```

## SQL-Beispiele

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
