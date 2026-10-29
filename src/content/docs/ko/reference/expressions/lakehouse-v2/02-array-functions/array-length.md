---
title: ARRAY_LENGTH (Lakehouse v2)
description: ARRAY_LENGTH — 배열의 요소 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-length.md
---

배열의 요소 수를 반환합니다.

## Analyze 구문

```python
func.array_length([1, 2, 3])
```

## Analyze 예제

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQL 구문

```sql
ARRAY_LENGTH([1, 2, 3])
```

## SQL 예제

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
