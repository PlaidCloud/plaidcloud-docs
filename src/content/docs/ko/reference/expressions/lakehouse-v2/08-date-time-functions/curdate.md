---
title: CURDATE (Lakehouse v2)
description: CURDATE — 현재 날짜를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curdate.md
---

현재 날짜를 반환합니다.

## Analyze 구문

```python
func.curdate()
```

## Analyze 예제

```python
func.curdate()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 구문

```sql
CURDATE()
```

## SQL 예제

```sql
SELECT CURDATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
