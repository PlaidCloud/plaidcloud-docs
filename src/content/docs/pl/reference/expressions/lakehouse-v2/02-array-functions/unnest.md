---
title: UNNEST (Lakehouse v2)
description: UNNEST — rozwija tablicę do zbioru wierszy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/unnest.md
---

Rozwija tablicę do zbioru wierszy.

## Składnia Analyze

```python
func.unnest([1, 2, 3])
```

## Przykłady Analyze

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## Składnia SQL

```sql
UNNEST([1, 2, 3])
```

## Przykłady SQL

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
