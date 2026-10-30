---
title: DATE_TRUNC (Lakehouse v2)
description: DATE_TRUNC — 날짜 또는 날짜/시간 값을 지정한 정밀도로 잘라냅니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-trunc.md
---

날짜 또는 날짜/시간 값을 지정한 정밀도로 잘라냅니다.

## Analyze 구문

```python
func.date_trunc(<unit>, <datetime>)
```

## Analyze 예제

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## SQL 구문

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## SQL 예제

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```
