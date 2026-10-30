---
title: DAY (Lakehouse v2)
description: DAY — 날짜에서 월 중 일을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/day.md
---

날짜에서 월 중 일을 반환합니다.

## Analyze 구문

```python
func.day(<date>)
```

## Analyze 예제

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQL 구문

```sql
DAY(<date>)
```

## SQL 예제

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```
