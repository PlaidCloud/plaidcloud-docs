---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME — 현재 시간을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-time.md
---

현재 시간을 반환합니다.

## Analyze 구문

```python
func.current_time()
```

## Analyze 예제

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL 구문

```sql
CURRENT_TIME()
```

## SQL 예제

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
