---
title: CURRENT_TIMEZONE (Lakehouse v2)
description: CURRENT_TIMEZONE — 현재 세션의 시간대를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timezone.md
---

현재 세션의 시간대를 반환합니다.

## Analyze 구문

```python
func.current_timezone()
```

## Analyze 예제

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## SQL 구문

```sql
CURRENT_TIMEZONE()
```

## SQL 예제

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```
