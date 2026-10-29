---
title: LEFT (Lakehouse v2)
description: LEFT — gibt die ersten N Zeichen einer Zeichenfolge von links zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

Gibt die ersten N Zeichen einer Zeichenfolge von links zurück.

## Analyze-Syntax

```python
func.left(<str>, <len>)
```

## Analyze-Beispiele

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL-Syntax

```sql
LEFT(<str>, <len>)
```

## SQL-Beispiele

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
