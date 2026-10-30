---
title: ALL_MATCH (Lakehouse v2)
description: ALL_MATCH — 배열의 모든 요소가 지정한 조건자와 일치하면 TRUE를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/all-match.md
---

배열의 모든 요소가 지정한 조건자와 일치하면 TRUE를 반환합니다.

## Analyze 구문

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Analyze 예제

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## SQL 예제

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
