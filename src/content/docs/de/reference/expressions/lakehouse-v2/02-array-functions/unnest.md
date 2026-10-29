---
title: UNNEST (Lakehouse v2)
description: UNNEST – erweitert ein Array zu einer Menge von Zeilen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/unnest.md
---

Erweitert ein Array zu einer Menge von Zeilen.

## Analyze-Syntax

```python
func.unnest([1, 2, 3])
```

## Analyze-Beispiele

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## SQL-Syntax

```sql
UNNEST([1, 2, 3])
```

## SQL-Beispiele

```sql
SELECT * FROM UNNEST([1, 2, 3]) AS t(val);

┌─────┐
│ val │
├─────┤
│   1 │
│   2 │
│   3 │
└─────┘
```
