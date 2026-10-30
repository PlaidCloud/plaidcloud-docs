---
title: DATEDIFF (Lakehouse v2)
description: DATEDIFF — zwraca liczbę dni między dwiema datami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/datediff.md
---

Zwraca liczbę dni między dwiema datami.

## Składnia Analyze

```python
func.datediff(<end_date>, <start_date>)
```

## Przykłady Analyze

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## Składnia SQL

```sql
DATEDIFF(<end_date>, <start_date>)
```

## Przykłady SQL

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
