---
title: ARRAY_REMOVE (Lakehouse v2)
description: ARRAY_REMOVE — 배열에서 지정한 요소를 모두 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-remove.md
---

배열에서 지정한 요소를 모두 제거합니다.

## Analyze 구문

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Analyze 예제

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## SQL 구문

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## SQL 예제

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```
