---
title: MONTH (Lakehouse v2)
description: MONTH — 날짜에서 월을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/month.md
---

날짜에서 월을 반환합니다.

## Analyze 구문

```python
func.month(<date>)
```

## Analyze 예제

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQL 구문

```sql
MONTH(<date>)
```

## SQL 예제

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```
