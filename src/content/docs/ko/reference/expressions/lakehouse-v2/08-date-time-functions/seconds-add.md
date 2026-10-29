---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD — 날짜/시간 값에 지정한 초 수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

날짜/시간 값에 지정한 초 수를 더합니다.

## Analyze 구문

```python
func.seconds_add(<datetime>, <n>)
```

## Analyze 예제

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## SQL 구문

```sql
SECONDS_ADD(<datetime>, <n>)
```

## SQL 예제

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```
