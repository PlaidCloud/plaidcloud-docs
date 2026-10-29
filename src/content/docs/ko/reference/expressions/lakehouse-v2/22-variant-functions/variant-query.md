---
title: VARIANT_QUERY (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 VARIANT_QUERY Variant 함수를 사용합니다. 경로 식을 사용하여 VARIANT 객체에서 값을 조회하고 VARIANT로 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

경로 식을 사용하여 VARIANT 객체에서 값을 조회하고 VARIANT로 반환합니다.

## Analyze 구문

```python
func.variant_query(<variant>, <path>)
```

## Analyze 예제

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## SQL 구문

```sql
VARIANT_QUERY(<variant>, <path>)
```

## SQL 예제

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
