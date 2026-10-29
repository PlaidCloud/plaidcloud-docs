---
title: SECONDS_DIFF (Lakehouse v2)
description: SECONDS_DIFF — 두 날짜/시간 값 사이의 초 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-diff.md
---

두 날짜/시간 값 사이의 초 수를 반환합니다.

## Analyze 구문

```python
func.seconds_diff(<end>, <start>)
```

## Analyze 예제

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## SQL 구문

```sql
SECONDS_DIFF(<end>, <start>)
```

## SQL 예제

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```
