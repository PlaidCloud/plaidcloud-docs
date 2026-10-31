---
title: SUBSTRING (Lakehouse v2)
description: SUBSTRING — gibt eine Teilzeichenfolge ab einer angegebenen Position zurück. Alias für `SUBSTR`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring.md
---

Gibt eine Teilzeichenfolge ab einer angegebenen Position zurück. Alias für `SUBSTR`.

## Analyze-Syntax

```python
func.substring(<str>, <pos>[, <len>])
```

## Analyze-Beispiele

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL-Syntax

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## SQL-Beispiele

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
