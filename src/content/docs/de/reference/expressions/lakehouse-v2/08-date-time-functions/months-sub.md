---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB – subtrahiert eine angegebene Anzahl von Monaten von einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-sub.md
---

Subtrahiert eine angegebene Anzahl von Monaten von einem Datum.

## Analyze-Syntax

```python
func.months_sub(<date>, <n>)
```

## Analyze-Beispiele

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
MONTHS_SUB(<date>, <n>)
```

## SQL-Beispiele

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```
