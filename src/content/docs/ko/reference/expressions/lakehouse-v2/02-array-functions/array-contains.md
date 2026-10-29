---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS — 배열이 특정 요소를 포함하는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains.md
---

배열이 특정 요소를 포함하는지 확인합니다.

## Analyze 구문

```python
func.array_contains([1, 2, 3], 2)
```

## Analyze 예제

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## SQL 예제

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
