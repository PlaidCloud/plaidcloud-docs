---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB — 날짜에서 지정한 연수를 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-sub.md
---

날짜에서 지정한 연수를 뺍니다.

## Analyze 구문

```python
func.years_sub(<date>, <n>)
```

## Analyze 예제

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL 구문

```sql
YEARS_SUB(<date>, <n>)
```

## SQL 예제

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
