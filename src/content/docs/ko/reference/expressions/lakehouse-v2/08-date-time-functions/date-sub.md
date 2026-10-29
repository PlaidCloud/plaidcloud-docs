---
title: DATE_SUB (Lakehouse v2)
description: DATE_SUB — 날짜 또는 날짜/시간에서 지정한 시간 간격을 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-sub.md
---

날짜 또는 날짜/시간에서 지정한 시간 간격을 뺍니다.

## Analyze 구문

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Analyze 예제

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## SQL 구문

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## SQL 예제

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```
