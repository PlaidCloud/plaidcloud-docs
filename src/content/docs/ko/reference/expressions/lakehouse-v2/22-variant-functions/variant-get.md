---
title: VARIANT_GET (Lakehouse v2)
description: VARIANT_GET — VARIANT 객체의 지정한 경로에서 형식이 지정된 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-get.md
---

VARIANT 객체의 지정한 경로에서 형식이 지정된 값을 추출합니다.

## Analyze 구문

```python
func.variant_get(<variant>, <path>, <type>)
```

## Analyze 예제

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## SQL 구문

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## SQL 예제

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
