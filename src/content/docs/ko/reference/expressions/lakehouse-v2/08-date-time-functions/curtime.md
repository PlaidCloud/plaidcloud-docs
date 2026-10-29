---
title: CURTIME (Lakehouse v2)
description: CURTIME — 현재 시간을 반환합니다. `CURRENT_TIME`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curtime.md
---

현재 시간을 반환합니다. `CURRENT_TIME`의 별칭입니다.

## Analyze 구문

```python
func.curtime()
```

## Analyze 예제

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL 구문

```sql
CURTIME()
```

## SQL 예제

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
