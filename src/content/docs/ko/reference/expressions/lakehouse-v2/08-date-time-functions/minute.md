---
title: MINUTE (Lakehouse v2)
description: MINUTE — 날짜/시간 값에서 분을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

날짜/시간 값에서 분을 반환합니다.

## Analyze 구문

```python
func.minute(<datetime>)
```

## Analyze 예제

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## SQL 구문

```sql
MINUTE(<datetime>)
```

## SQL 예제

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```
