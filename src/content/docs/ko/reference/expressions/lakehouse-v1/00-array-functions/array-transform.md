---
title: ARRAY_TRANSFORM (Lakehouse v1)
description: ARRAY_TRANSFORM — 입력 배열의 각 요소에 람다 함수를 적용한 결과로 이루어진 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-transform.md
---

입력 배열의 각 요소에 람다 함수를 적용한 결과로 이루어진 배열을 반환합니다.

## Analyze 구문

```python
func.array_transform( <array>, <lambda> )
```

## Analyze 예제

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## 별칭

- [ARRAY_APPLY](../array-apply)

## SQL 예제

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
