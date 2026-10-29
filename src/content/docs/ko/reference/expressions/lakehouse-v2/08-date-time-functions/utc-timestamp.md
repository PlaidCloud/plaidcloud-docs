---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP — 현재 UTC 날짜와 시간을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

현재 UTC 날짜와 시간을 반환합니다.

## Analyze 구문

```python
func.utc_timestamp()
```

## Analyze 예제

```python
func.utc_timestamp()

┌───────────────────────┐
│ '2024-06-15 18:30:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
UTC_TIMESTAMP()
```

## SQL 예제

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```
