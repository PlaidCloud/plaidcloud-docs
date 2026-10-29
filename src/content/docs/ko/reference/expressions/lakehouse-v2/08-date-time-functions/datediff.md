---
title: DATEDIFF (Lakehouse v2)
description: DATEDIFF — 두 날짜 사이의 일수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/datediff.md
---

두 날짜 사이의 일수를 반환합니다.

## Analyze 구문

```python
func.datediff(<end_date>, <start_date>)
```

## Analyze 예제

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## SQL 구문

```sql
DATEDIFF(<end_date>, <start_date>)
```

## SQL 예제

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
