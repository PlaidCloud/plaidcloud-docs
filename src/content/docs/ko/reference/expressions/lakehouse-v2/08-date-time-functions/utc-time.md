---
title: UTC_TIME (Lakehouse v2)
description: UTC_TIME — 현재 UTC 시간을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-time.md
---

현재 UTC 시간을 반환합니다.

## Analyze 구문

```python
func.utc_time()
```

## Analyze 예제

```python
func.utc_time()

┌────────────┐
│ '18:30:00'  │
└────────────┘
```

## SQL 구문

```sql
UTC_TIME()
```

## SQL 예제

```sql
SELECT UTC_TIME();

┌──────────┐
│ 18:30:00  │
└──────────┘
```
