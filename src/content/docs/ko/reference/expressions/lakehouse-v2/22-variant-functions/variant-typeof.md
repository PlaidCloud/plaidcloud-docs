---
title: VARIANT_TYPEOF (Lakehouse v2)
description: VARIANT_TYPEOF — VARIANT 값의 형식 이름을 문자열로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-typeof.md
---

VARIANT 값의 형식 이름을 문자열로 반환합니다.

## Analyze 구문

```python
func.variant_typeof(<variant>)
```

## Analyze 예제

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## SQL 구문

```sql
VARIANT_TYPEOF(<variant>)
```

## SQL 예제

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
