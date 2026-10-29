---
title: DATE_FORMAT (Lakehouse v2)
description: DATE_FORMAT — 형식 문자열에 따라 날짜 또는 날짜/시간 값의 형식을 지정합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-format.md
---

형식 문자열에 따라 날짜 또는 날짜/시간 값의 형식을 지정합니다.

## Analyze 구문

```python
func.date_format(<date>, <format>)
```

## Analyze 예제

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQL 구문

```sql
DATE_FORMAT(<date>, <format>)
```

## SQL 예제

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
