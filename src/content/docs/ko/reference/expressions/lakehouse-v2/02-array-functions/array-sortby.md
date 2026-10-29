---
title: ARRAY_SORTBY (Lakehouse v2)
description: ARRAY_SORTBY — 다른 배열의 대응하는 요소를 기준으로 한 배열의 요소를 정렬합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sortby.md
---

다른 배열의 대응하는 요소를 기준으로 한 배열의 요소를 정렬합니다.

## Analyze 구문

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Analyze 예제

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL 구문

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## SQL 예제

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
