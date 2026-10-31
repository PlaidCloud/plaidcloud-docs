---
title: ARRAY_MAX (Lakehouse v2)
description: ARRAY_MAX – gibt das größte Element eines Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-max.md
---

Gibt das größte Element eines Arrays zurück.

## Analyze-Syntax

```python
func.array_max([3, 1, 4, 1, 5])
```

## Analyze-Beispiele

```python
func.array_max([3, 1, 4, 1, 5])

┌───┐
│ 5 │
└───┘
```

## SQL-Syntax

```sql
ARRAY_MAX([3, 1, 4, 1, 5])
```

## SQL-Beispiele

```sql
SELECT ARRAY_MAX([3, 1, 4, 1, 5]);

┌───┐
│ 5 │
└───┘
```
