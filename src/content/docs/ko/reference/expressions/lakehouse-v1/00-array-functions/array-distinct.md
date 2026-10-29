---
title: ARRAY_DISTINCT (Lakehouse v1)
description: ARRAY_DISTINCT — 원래 순서를 유지하지 않고 배열에서 중복 요소와 NULL을 모두 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-distinct.md
---

원래 순서를 유지하지 않고 배열에서 중복 요소와 NULL을 모두 제거합니다.

## Analyze 구문

```python
func.array_distinct( <array> )
```

## Analyze 예제

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_DISTINCT( <array> )
```

## SQL 예제

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```
