---
title: ARRAY_MIN (Lakehouse v2)
description: ARRAY_MIN — 배열에서 가장 작은 요소를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-min.md
---

배열에서 가장 작은 요소를 반환합니다.

## Analyze 구문

```python
func.array_min([3, 1, 4, 1, 5])
```

## Analyze 예제

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## SQL 예제

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
