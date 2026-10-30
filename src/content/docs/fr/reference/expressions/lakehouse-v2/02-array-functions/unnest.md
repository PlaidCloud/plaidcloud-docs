---
title: UNNEST (Lakehouse v2)
description: UNNEST — développe un tableau en un ensemble de lignes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/unnest.md
---

Développe un tableau en un ensemble de lignes.

## Syntaxe Analyze

```python
func.unnest([1, 2, 3])
```

## Exemples Analyze

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## Syntaxe SQL

```sql
UNNEST([1, 2, 3])
```

## Exemples SQL

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
