---
title: SUBDATE (Lakehouse v2)
description: SUBDATE — 날짜에서 시간 간격을 뺍니다. `DATE_SUB`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/subdate.md
---

날짜에서 시간 간격을 뺍니다. `DATE_SUB`의 별칭입니다.

## Analyze 구문

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Analyze 예제

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## SQL 구문

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## SQL 예제

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```
