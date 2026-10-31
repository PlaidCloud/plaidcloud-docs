---
title: ENDS_WITH (Lakehouse v2)
description: ENDS_WITH — Prüft, ob eine Zeichenfolge mit einem angegebenen Suffix endet.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ends-with.md
---

Prüft, ob eine Zeichenfolge mit einem angegebenen Suffix endet.

## Analyze-Syntax

```python
func.ends_with(<str>, <suffix>)
```

## Analyze-Beispiele

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
ENDS_WITH(<str>, <suffix>)
```

## SQL-Beispiele

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
