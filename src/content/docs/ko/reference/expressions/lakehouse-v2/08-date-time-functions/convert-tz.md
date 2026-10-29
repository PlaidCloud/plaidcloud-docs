---
title: CONVERT_TZ (Lakehouse v2)
description: CONVERT_TZ — 날짜/시간을 한 시간대에서 다른 시간대로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/convert-tz.md
---

날짜/시간을 한 시간대에서 다른 시간대로 변환합니다.

## Analyze 구문

```python
func.convert_tz(<datetime>, <from_tz>, <to_tz>)
```

## Analyze 예제

```python
func.convert_tz('2024-01-01 12:00:00', 'UTC', 'America/New_York')

┌───────────────────────┐
│ '2024-01-01 07:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
CONVERT_TZ(<datetime>, <from_tz>, <to_tz>)
```

## SQL 예제

```sql
SELECT CONVERT_TZ('2024-01-01 12:00:00', 'UTC', 'America/New_York');

┌─────────────────────┐
│ 2024-01-01 07:00:00  │
└─────────────────────┘
```
