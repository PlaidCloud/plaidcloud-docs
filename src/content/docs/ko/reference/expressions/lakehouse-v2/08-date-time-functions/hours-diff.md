---
title: HOURS_DIFF (Lakehouse v2)
description: HOURS_DIFF — 두 날짜/시간 사이의 시간 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-diff.md
---

두 날짜/시간 사이의 시간 수를 반환합니다.

## Analyze 구문

```python
func.hours_diff(<end>, <start>)
```

## Analyze 예제

```python
func.hours_diff('2024-01-02 10:00:00', '2024-01-01 10:00:00')

┌────┐
│ 24  │
└────┘
```

## SQL 구문

```sql
HOURS_DIFF(<end>, <start>)
```

## SQL 예제

```sql
SELECT HOURS_DIFF('2024-01-02 10:00:00', '2024-01-01 10:00:00');

┌────┐
│ 24  │
└────┘
```
