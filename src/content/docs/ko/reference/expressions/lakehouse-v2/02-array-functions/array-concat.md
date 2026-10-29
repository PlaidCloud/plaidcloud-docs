---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT — 여러 배열을 하나의 배열로 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

여러 배열을 하나의 배열로 연결합니다.

## Analyze 구문

```python
func.array_concat([1, 2], [3, 4])
```

## Analyze 예제

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL 구문

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## SQL 예제

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
