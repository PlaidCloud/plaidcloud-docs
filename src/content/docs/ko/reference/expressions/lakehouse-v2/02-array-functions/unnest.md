---
title: UNNEST (Lakehouse v2)
description: UNNEST — 배열을 행 집합으로 펼칩니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/unnest.md
---

배열을 행 집합으로 펼칩니다.

## Analyze 구문

```python
func.unnest([1, 2, 3])
```

## Analyze 예제

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## SQL 구문

```sql
UNNEST([1, 2, 3])
```

## SQL 예제

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
