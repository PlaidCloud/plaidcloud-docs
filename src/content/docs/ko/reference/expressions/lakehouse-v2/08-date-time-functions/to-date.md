---
title: TO_DATE (Lakehouse v2)
description: TO_DATE — 날짜/시간 값을 날짜로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

날짜/시간 값을 날짜로 변환합니다.

## Analyze 구문

```python
func.to_date(<datetime>)
```

## Analyze 예제

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 구문

```sql
TO_DATE(<datetime>)
```

## SQL 예제

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
