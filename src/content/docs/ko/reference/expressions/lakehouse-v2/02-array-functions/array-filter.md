---
title: ARRAY_FILTER (Lakehouse v2)
description: ARRAY_FILTER — 람다 식을 사용하여 배열의 요소를 필터링합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-filter.md
---

람다 식을 사용하여 배열의 요소를 필터링합니다.

## Analyze 구문

```python
func.array_filter(get_column(table, 'arr'), lambda x: x > 2)
```

## Analyze 예제

```python
func.array_filter([1, 2, 3, 4, 5], lambda x: x > 2)

┌─────────┐
│ [3,4,5] │
└─────────┘
```

## SQL 구문

```sql
ARRAY_FILTER(<arr>, lambda x: x > 2)
```

## SQL 예제

```sql
SELECT ARRAY_FILTER([1, 2, 3, 4, 5], x -> x > 2);

┌─────────┐
│ [3,4,5] │
└─────────┘
```
