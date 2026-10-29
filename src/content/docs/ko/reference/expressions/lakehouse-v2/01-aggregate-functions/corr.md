---
title: CORR (Lakehouse v2)
description: CORR — 두 식 사이의 피어슨 상관 계수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/corr.md
---

두 식 사이의 피어슨 상관 계수를 반환합니다.

## Analyze 구문

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Analyze 예제

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## SQL 구문

```sql
CORR(<revenue>, <ad_spend>)
```

## SQL 예제

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
