---
title: ARRAY_FLATTEN (Lakehouse v1)
description: ARRAY_FLATTEN — 중첩 배열을 단일 수준 배열로 평탄화합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-flatten.md
---

중첩 배열을 단일 수준 배열로 평탄화합니다.

## Analyze 구문

```python
func.array_flatten( <array> )
```

## Analyze 예제

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_FLATTEN( <array> )
```

## SQL 예제

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```
