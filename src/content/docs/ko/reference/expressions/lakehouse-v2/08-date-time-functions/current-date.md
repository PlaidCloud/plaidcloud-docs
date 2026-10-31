---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE — 현재 날짜를 반환합니다. `CURDATE`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-date.md
---

현재 날짜를 반환합니다. `CURDATE`의 별칭입니다.

## Analyze 구문

```python
func.current_date()
```

## Analyze 예제

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 구문

```sql
CURRENT_DATE()
```

## SQL 예제

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
