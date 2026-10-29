---
title: MONTHS_DIFF (Lakehouse v2)
description: MONTHS_DIFF — 두 날짜 사이의 개월 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-diff.md
---

두 날짜 사이의 개월 수를 반환합니다.

## Analyze 구문

```python
func.months_diff(<end_date>, <start_date>)
```

## Analyze 예제

```python
func.months_diff('2024-06-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## SQL 구문

```sql
MONTHS_DIFF(<end_date>, <start_date>)
```

## SQL 예제

```sql
SELECT MONTHS_DIFF('2024-06-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
