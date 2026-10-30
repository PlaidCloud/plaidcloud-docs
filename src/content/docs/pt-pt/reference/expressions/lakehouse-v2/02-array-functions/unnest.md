---
title: UNNEST (Lakehouse v2)
description: UNNEST — expande uma matriz num conjunto de linhas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/unnest.md
---

Expande uma matriz num conjunto de linhas.

## Sintaxe do Analyze

```python
func.unnest([1, 2, 3])
```

## Exemplos do Analyze

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## Sintaxe SQL

```sql
UNNEST([1, 2, 3])
```

## Exemplos SQL

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
