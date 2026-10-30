---
title: "REVERSE (Zeichenfolge, Lakehouse v2)"
description: REVERSE — kehrt eine Zeichenfolge um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

Kehrt eine Zeichenfolge um.

## Analyze-Syntax

```python
func.reverse(<str>)
```

## Analyze-Beispiele

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## SQL-Syntax

```sql
REVERSE(<str>)
```

## SQL-Beispiele

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
