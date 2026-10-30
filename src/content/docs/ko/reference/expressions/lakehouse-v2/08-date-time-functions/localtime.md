---
title: LOCALTIME (Lakehouse v2)
description: LOCALTIME — 현재 날짜와 시간을 반환합니다. `NOW`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtime.md
---

현재 날짜와 시간을 반환합니다. `NOW`의 별칭입니다.

## Analyze 구문

```python
func.localtime()
```

## Analyze 예제

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
LOCALTIME()
```

## SQL 예제

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
