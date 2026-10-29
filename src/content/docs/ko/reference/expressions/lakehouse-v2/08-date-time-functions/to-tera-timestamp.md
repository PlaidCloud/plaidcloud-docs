---
title: TO_TERA_TIMESTAMP (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 TO_TERA_TIMESTAMP 날짜/시간 함수를 사용합니다. Teradata 형식 문자열에 따라 VARCHAR 값을 DATETIME 값으로 변환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-timestamp.md
---

Teradata 형식 문자열에 따라 VARCHAR 값을 DATETIME 값으로 변환합니다.

## Analyze 구문

```python
func.to_tera_timestamp(<str>, <format>)
```

## Analyze 예제

```python
func.to_tera_timestamp('20240615143000', 'YYYYMMDDHH24MISS')

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
TO_TERA_TIMESTAMP(<str>, <format>)
```

## SQL 예제

```sql
SELECT TO_TERA_TIMESTAMP('20240615143000', 'YYYYMMDDHH24MISS');

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
