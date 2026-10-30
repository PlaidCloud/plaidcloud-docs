---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS — 일수를 날짜로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-days.md
---

일수를 날짜로 변환합니다.

## Analyze 구문

```python
func.from_days(<n>)
```

## Analyze 예제

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL 구문

```sql
FROM_DAYS(<n>)
```

## SQL 예제

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
