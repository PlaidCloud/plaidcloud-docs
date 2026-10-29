---
title: ANY_MATCH (Lakehouse v2)
description: ANY_MATCH — 배열의 요소 중 하나라도 지정한 조건자와 일치하면 TRUE를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/any-match.md
---

배열의 요소 중 하나라도 지정한 조건자와 일치하면 TRUE를 반환합니다.

## Analyze 구문

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Analyze 예제

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## SQL 예제

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
