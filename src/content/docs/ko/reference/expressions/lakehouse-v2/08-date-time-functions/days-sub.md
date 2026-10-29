---
title: DAYS_SUB (Lakehouse v2)
description: DAYS_SUB — 날짜에서 지정한 일수를 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-sub.md
---

날짜에서 지정한 일수를 뺍니다.

## Analyze 구문

```python
func.days_sub(<date>, <n>)
```

## Analyze 예제

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL 구문

```sql
DAYS_SUB(<date>, <n>)
```

## SQL 예제

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
