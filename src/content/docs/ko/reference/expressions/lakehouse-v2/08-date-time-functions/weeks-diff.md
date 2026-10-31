---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF — 두 날짜 사이의 주 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-diff.md
---

두 날짜 사이의 주 수를 반환합니다.

## Analyze 구문

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Analyze 예제

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## SQL 구문

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## SQL 예제

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```
