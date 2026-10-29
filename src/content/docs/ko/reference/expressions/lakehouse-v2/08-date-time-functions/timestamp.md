---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP — 날짜 또는 문자열을 날짜/시간 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestamp.md
---

날짜 또는 문자열을 날짜/시간 값으로 변환합니다.

## Analyze 구문

```python
func.timestamp(<expr>)
```

## Analyze 예제

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
TIMESTAMP(<expr>)
```

## SQL 예제

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
