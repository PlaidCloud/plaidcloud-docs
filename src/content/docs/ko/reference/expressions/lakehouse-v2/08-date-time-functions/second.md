---
title: SECOND (Lakehouse v2)
description: SECOND — 날짜/시간 값에서 초를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

날짜/시간 값에서 초를 반환합니다.

## Analyze 구문

```python
func.second(<datetime>)
```

## Analyze 예제

```python
func.second('2024-06-15 14:30:45')

┌────┐
│ 45  │
└────┘
```

## SQL 구문

```sql
SECOND(<datetime>)
```

## SQL 예제

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```
