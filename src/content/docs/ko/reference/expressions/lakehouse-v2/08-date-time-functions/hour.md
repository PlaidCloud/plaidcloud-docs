---
title: HOUR (Lakehouse v2)
description: HOUR — 날짜/시간에서 시를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hour.md
---

날짜/시간에서 시를 반환합니다.

## Analyze 구문

```python
func.hour(<datetime>)
```

## Analyze 예제

```python
func.hour('2024-06-15 14:30:00')

┌────┐
│ 14  │
└────┘
```

## SQL 구문

```sql
HOUR(<datetime>)
```

## SQL 예제

```sql
SELECT HOUR('2024-06-15 14:30:00');

┌────┐
│ 14  │
└────┘
```
