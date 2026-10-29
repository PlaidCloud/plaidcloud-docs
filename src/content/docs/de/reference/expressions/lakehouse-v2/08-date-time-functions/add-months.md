---
title: ADD_MONTHS (Lakehouse v2)
description: ADD_MONTHS – addiert eine angegebene Anzahl von Monaten zu einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/add-months.md
---

Addiert eine angegebene Anzahl von Monaten zu einem Datum.

## Analyze-Syntax

```python
func.add_months(<date>, <months>)
```

## Analyze-Beispiele

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQL-Syntax

```sql
ADD_MONTHS(<date>, <months>)
```

## SQL-Beispiele

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
