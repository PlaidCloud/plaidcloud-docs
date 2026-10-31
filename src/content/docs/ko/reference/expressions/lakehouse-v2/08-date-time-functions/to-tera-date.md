---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — Teradata 형식 문자열에 따라 VARCHAR 값을 DATE 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

Teradata 형식 문자열에 따라 VARCHAR 값을 DATE 값으로 변환합니다.

## Analyze 구문

```python
func.to_tera_date(<str>, <format>)
```

## Analyze 예제

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 구문

```sql
TO_TERA_DATE(<str>, <format>)
```

## SQL 예제

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
