---
title: ARRAY_MAP (Lakehouse v2)
description: ARRAY_MAP — 배열의 각 요소에 람다 식을 적용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-map.md
---

배열의 각 요소에 람다 식을 적용합니다.

## Analyze 구문

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Analyze 예제

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## SQL 구문

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## SQL 예제

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```
