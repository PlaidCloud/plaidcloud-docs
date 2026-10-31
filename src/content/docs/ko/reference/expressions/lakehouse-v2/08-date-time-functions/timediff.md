---
title: TIMEDIFF (Lakehouse v2)
description: TIMEDIFF — 두 시간 값의 차이를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timediff.md
---

두 시간 값의 차이를 반환합니다.

## Analyze 구문

```python
func.timediff(<time1>, <time2>)
```

## Analyze 예제

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## SQL 구문

```sql
TIMEDIFF(<time1>, <time2>)
```

## SQL 예제

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```
