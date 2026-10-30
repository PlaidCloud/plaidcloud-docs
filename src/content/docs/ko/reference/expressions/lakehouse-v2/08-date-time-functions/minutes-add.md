---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — 날짜/시간 값에 지정한 분 수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

날짜/시간 값에 지정한 분 수를 더합니다.

## Analyze 구문

```python
func.minutes_add(<datetime>, <n>)
```

## Analyze 예제

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
MINUTES_ADD(<datetime>, <n>)
```

## SQL 예제

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
