---
title: RIGHT (Lakehouse v2)
description: RIGHT — gibt die letzten N Zeichen einer Zeichenfolge von rechts zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

Gibt die letzten N Zeichen einer Zeichenfolge von rechts zurück.

## Analyze-Syntax

```python
func.right(<str>, <len>)
```

## Analyze-Beispiele

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL-Syntax

```sql
RIGHT(<str>, <len>)
```

## SQL-Beispiele

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
