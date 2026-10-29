---
title: ADD_MONTHS (Lakehouse v2)
description: ADD_MONTHS — 날짜에 지정한 개월 수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/add-months.md
---

날짜에 지정한 개월 수를 더합니다.

## Analyze 구문

```python
func.add_months(<date>, <months>)
```

## Analyze 예제

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQL 구문

```sql
ADD_MONTHS(<date>, <months>)
```

## SQL 예제

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
