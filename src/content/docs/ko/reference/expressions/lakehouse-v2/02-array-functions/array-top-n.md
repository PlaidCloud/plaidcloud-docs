---
title: ARRAY_TOP_N (Lakehouse v2)
description: ARRAY_TOP_N — 배열에서 상위 N개의 요소를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-top-n.md
---

배열에서 상위 N개의 요소를 반환합니다.

## Analyze 구문

```python
func.array_top_n([3,1,4,1,5], 3)
```

## Analyze 예제

```python
func.array_top_n([3, 1, 4, 1, 5], 3)

┌─────────┐
│ [5,4,3] │
└─────────┘
```

## SQL 구문

```sql
ARRAY_TOP_N([3,1,4,1,5], 3)
```

## SQL 예제

```sql
SELECT ARRAY_TOP_N([3, 1, 4, 1, 5], 3);

┌─────────┐
│ [5,4,3] │
└─────────┘
```
