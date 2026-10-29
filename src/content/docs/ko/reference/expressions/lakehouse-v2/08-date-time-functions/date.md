---
title: DATE (Lakehouse v2)
description: DATE — 날짜/시간 식에서 날짜 부분을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date.md
---

날짜/시간 식에서 날짜 부분을 추출합니다.

## Analyze 구문

```python
func.date(<datetime>)
```

## Analyze 예제

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 구문

```sql
DATE(<datetime>)
```

## SQL 예제

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
