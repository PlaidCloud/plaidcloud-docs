---
title: YEARS_DIFF (Lakehouse v2)
description: YEARS_DIFF — 두 날짜 사이의 연수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-diff.md
---

두 날짜 사이의 연수를 반환합니다.

## Analyze 구문

```python
func.years_diff(<end_date>, <start_date>)
```

## Analyze 예제

```python
func.years_diff('2029-01-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## SQL 구문

```sql
YEARS_DIFF(<end_date>, <start_date>)
```

## SQL 예제

```sql
SELECT YEARS_DIFF('2029-01-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
