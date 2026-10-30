---
title: UNNEST (Lakehouse v2)
description: UNNEST — expande una matriz en un conjunto de filas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/unnest.md
---

Expande una matriz en un conjunto de filas.

## Sintaxis de Analyze

```python
func.unnest([1, 2, 3])
```

## Ejemplos de Analyze

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## Sintaxis de SQL

```sql
UNNEST([1, 2, 3])
```

## Ejemplos de SQL

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
