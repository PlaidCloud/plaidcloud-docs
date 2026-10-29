---
title: TO_DATETIME (Lakehouse v2)
description: TO_DATETIME — 값을 날짜/시간 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime.md
---

값을 날짜/시간 값으로 변환합니다.

## Analyze 구문

```python
func.to_datetime(<expr>)
```

## Analyze 예제

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
TO_DATETIME(<expr>)
```

## SQL 예제

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
