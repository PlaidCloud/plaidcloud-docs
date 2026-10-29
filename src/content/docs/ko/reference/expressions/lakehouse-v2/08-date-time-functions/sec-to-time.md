---
title: SEC_TO_TIME (Lakehouse v2)
description: SEC_TO_TIME — 초를 시간 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/sec-to-time.md
---

초를 시간 값으로 변환합니다.

## Analyze 구문

```python
func.sec_to_time(<seconds>)
```

## Analyze 예제

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## SQL 구문

```sql
SEC_TO_TIME(<seconds>)
```

## SQL 예제

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```
