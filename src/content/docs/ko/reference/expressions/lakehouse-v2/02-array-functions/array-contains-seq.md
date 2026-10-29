---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ — 배열이 다른 배열의 모든 요소를 같은 순서로 포함하는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

배열이 다른 배열의 모든 요소를 같은 순서로 포함하는지 확인합니다.

## Analyze 구문

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Analyze 예제

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## SQL 예제

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```
