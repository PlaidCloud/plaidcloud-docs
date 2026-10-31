---
title: MICROSECONDS_ADD (Lakehouse v2)
description: MICROSECONDS_ADD — 날짜/시간 값에 지정한 마이크로초 수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-add.md
---

날짜/시간 값에 지정한 마이크로초 수를 더합니다.

## Analyze 구문

```python
func.microseconds_add(<datetime>, <n>)
```

## Analyze 예제

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## SQL 구문

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## SQL 예제

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```
