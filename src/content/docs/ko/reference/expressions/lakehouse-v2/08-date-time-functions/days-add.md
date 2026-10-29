---
title: DAYS_ADD (Lakehouse v2)
description: DAYS_ADD — 날짜에 지정한 일수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-add.md
---

날짜에 지정한 일수를 더합니다.

## Analyze 구문

```python
func.days_add(<date>, <n>)
```

## Analyze 예제

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQL 구문

```sql
DAYS_ADD(<date>, <n>)
```

## SQL 예제

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
