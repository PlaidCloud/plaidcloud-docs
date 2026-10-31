---
title: ADD_MONTHS (Lakehouse v2)
description: ADD_MONTHS — dodaje do daty podaną liczbę miesięcy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/add-months.md
---

Dodaje do daty podaną liczbę miesięcy.

## Składnia Analyze

```python
func.add_months(<date>, <months>)
```

## Przykłady Analyze

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## Składnia SQL

```sql
ADD_MONTHS(<date>, <months>)
```

## Przykłady SQL

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
