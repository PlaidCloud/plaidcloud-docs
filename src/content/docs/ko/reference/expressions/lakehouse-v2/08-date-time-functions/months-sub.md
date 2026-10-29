---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB — 날짜에서 지정한 개월 수를 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-sub.md
---

날짜에서 지정한 개월 수를 뺍니다.

## Analyze 구문

```python
func.months_sub(<date>, <n>)
```

## Analyze 예제

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## SQL 구문

```sql
MONTHS_SUB(<date>, <n>)
```

## SQL 예제

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```
