---
title: WEEKDAY (Lakehouse v2)
description: WEEKDAY — 날짜의 요일 인덱스를 반환합니다(0=월요일, 6=일요일).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekday.md
---

날짜의 요일 인덱스를 반환합니다(0=월요일, 6=일요일).

## Analyze 구문

```python
func.weekday(<date>)
```

## Analyze 예제

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## SQL 구문

```sql
WEEKDAY(<date>)
```

## SQL 예제

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```
