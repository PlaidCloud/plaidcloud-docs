---
title: ARRAY_FILTER (Lakehouse v1)
description: ARRAY_FILTER — 람다 함수가 true를 반환하는 입력 배열의 요소로 새 배열을 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-filter.md
---

람다 함수가 true를 반환하는 입력 배열의 요소로 새 배열을 만듭니다.

## Analyze 구문

```python
func.array_filter( <array>, <lambda> )
```

## Analyze 예제

```python
func.array_filter([1, 2, 3], x -> (x > 1))

┌─────────────────────────────────────────────┐
│ func.array_filter([1, 2, 3], x -> (x > 1))  │
├─────────────────────────────────────────────┤
│ [2,3]                                       │
└─────────────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_FILTER( <array>, <lambda> )
```

## SQL 예제

```sql
SELECT ARRAY_FILTER([1, 2, 3], x -> x > 1);

┌───────────────────────────────────────┐
│ array_filter([1, 2, 3], x -> (x > 1)) │
├───────────────────────────────────────┤
│ [2,3]                                 │
└───────────────────────────────────────┘
```
