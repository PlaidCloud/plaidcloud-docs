---
title: DATE_ADD (Lakehouse v2)
description: DATE_ADD — 날짜 또는 날짜/시간에 지정한 시간 간격을 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-add.md
---

날짜 또는 날짜/시간에 지정한 시간 간격을 더합니다.

## Analyze 구문

```python
func.date_add(<date>, INTERVAL <n> <unit>)
```

## Analyze 예제

```python
func.date_add('2024-01-01', text('INTERVAL 30 DAY'))

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQL 구문

```sql
DATE_ADD(<date>, INTERVAL <n> <unit>)
```

## SQL 예제

```sql
SELECT DATE_ADD('2024-01-01', INTERVAL 30 DAY);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
