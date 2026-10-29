---
title: MILLISECONDS_DIFF (Lakehouse v2)
description: MILLISECONDS_DIFF — 두 날짜/시간 값 사이의 밀리초 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/milliseconds-diff.md
---

두 날짜/시간 값 사이의 밀리초 수를 반환합니다.

## Analyze 구문

```python
func.milliseconds_diff(<end>, <start>)
```

## Analyze 예제

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## SQL 구문

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## SQL 예제

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```
