---
title: STARTS_WITH (Lakehouse v2)
description: STARTS_WITH — Prüft, ob eine Zeichenfolge mit einem angegebenen Präfix beginnt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/starts-with.md
---

Prüft, ob eine Zeichenfolge mit einem angegebenen Präfix beginnt.

## Analyze-Syntax

```python
func.starts_with(<str>, <prefix>)
```

## Analyze-Beispiele

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
STARTS_WITH(<str>, <prefix>)
```

## SQL-Beispiele

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
