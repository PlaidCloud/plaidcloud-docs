---
title: ARRAY_JOIN (Lakehouse v2)
description: ARRAY_JOIN — 구분자를 사용하여 배열 요소를 하나의 문자열로 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-join.md
---

구분자를 사용하여 배열 요소를 하나의 문자열로 연결합니다.

## Analyze 구문

```python
func.array_join([1,2,3], '-')
```

## Analyze 예제

```python
func.array_join(['a', 'b', 'c'], '-')

┌─────────┐
│ 'a-b-c' │
└─────────┘
```

## SQL 구문

```sql
ARRAY_JOIN([1,2,3], '-')
```

## SQL 예제

```sql
SELECT ARRAY_JOIN(['a', 'b', 'c'], '-');

┌───────┐
│ a-b-c │
└───────┘
```
