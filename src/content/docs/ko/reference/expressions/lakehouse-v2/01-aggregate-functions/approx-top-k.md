---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K — 가장 자주 나타나는 상위 k개 값과 해당 근사 개수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

가장 자주 나타나는 상위 k개 값과 해당 근사 개수를 반환합니다.

## Analyze 구문

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Analyze 예제

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## SQL 구문

```sql
APPROX_TOP_K(<city>, 3)
```

## SQL 예제

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
