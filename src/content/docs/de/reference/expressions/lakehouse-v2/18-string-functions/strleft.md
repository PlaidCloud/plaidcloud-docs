---
title: STRLEFT (Lakehouse v2)
description: STRLEFT — gibt die ersten N Zeichen einer Zeichenfolge von links zurück. Alias für `LEFT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strleft.md
---

Gibt die ersten N Zeichen einer Zeichenfolge von links zurück. Alias für `LEFT`.

## Analyze-Syntax

```python
func.strleft(<str>, <len>)
```

## Analyze-Beispiele

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL-Syntax

```sql
STRLEFT(<str>, <len>)
```

## SQL-Beispiele

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
