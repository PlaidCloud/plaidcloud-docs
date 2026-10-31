---
title: ARRAY_APPEND (Lakehouse v2)
description: ARRAY_APPEND — 배열의 끝에 요소를 추가합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-append.md
---

배열의 끝에 요소를 추가합니다.

## Analyze 구문

```python
func.array_append([1, 2, 3], 4)
```

## Analyze 예제

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL 구문

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## SQL 예제

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
