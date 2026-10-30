---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS — 날짜를 일수로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-days.md
---

날짜를 일수로 변환합니다.

## Analyze 구문

```python
func.to_days(<date>)
```

## Analyze 예제

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## SQL 구문

```sql
TO_DAYS(<date>)
```

## SQL 예제

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```
