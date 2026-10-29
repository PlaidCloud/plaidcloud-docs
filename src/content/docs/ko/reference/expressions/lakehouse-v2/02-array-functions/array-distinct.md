---
title: ARRAY_DISTINCT (Lakehouse v2)
description: ARRAY_DISTINCT — 배열에서 중복된 요소를 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-distinct.md
---

배열에서 중복된 요소를 제거합니다.

## Analyze 구문

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Analyze 예제

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## SQL 구문

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## SQL 예제

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```
