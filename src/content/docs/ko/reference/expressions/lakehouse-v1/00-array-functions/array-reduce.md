---
title: ARRAY_REDUCE (Lakehouse v1)
description: ARRAY_REDUCE — 람다 함수를 배열의 요소에 반복 적용하여 배열을 단일 값으로 축소합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-reduce.md
---

람다 함수를 배열의 요소에 반복 적용하여 배열을 단일 값으로 축소합니다.

## Analyze 구문

```python
func.array_reduce( <array>, <lambda> )
```

## Analyze 예제

```python
func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))

┌─────────────────────────────────────────────────────┐
│ func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))  │
├─────────────────────────────────────────────────────┤
│                                                  10 │
└─────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_REDUCE( <array>, <lambda> )
```

## SQL 예제

```sql
SELECT ARRAY_REDUCE([1, 2, 3, 4], (x,y) -> x + y);

┌───────────────────────────────────────────────┐
│ array_reduce([1, 2, 3, 4], (x, y) -> (x + y)) │
├───────────────────────────────────────────────┤
│                                            10 │
└───────────────────────────────────────────────┘
```
