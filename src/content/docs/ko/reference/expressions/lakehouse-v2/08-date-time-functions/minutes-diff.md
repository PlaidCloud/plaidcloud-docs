---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF — 두 날짜/시간 값 사이의 분 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-diff.md
---

두 날짜/시간 값 사이의 분 수를 반환합니다.

## Analyze 구문

```python
func.minutes_diff(<end>, <start>)
```

## Analyze 예제

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## SQL 구문

```sql
MINUTES_DIFF(<end>, <start>)
```

## SQL 예제

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```
