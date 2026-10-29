---
title: HOURS_ADD (Lakehouse v2)
description: HOURS_ADD — 날짜/시간에 지정한 시간 수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-add.md
---

날짜/시간에 지정한 시간 수를 더합니다.

## Analyze 구문

```python
func.hours_add(<datetime>, <n>)
```

## Analyze 예제

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
HOURS_ADD(<datetime>, <n>)
```

## SQL 예제

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```
