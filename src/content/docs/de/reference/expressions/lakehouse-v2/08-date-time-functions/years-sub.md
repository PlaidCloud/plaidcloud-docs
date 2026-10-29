---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB – subtrahiert eine angegebene Anzahl von Jahren von einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-sub.md
---

Subtrahiert eine angegebene Anzahl von Jahren von einem Datum.

## Analyze-Syntax

```python
func.years_sub(<date>, <n>)
```

## Analyze-Beispiele

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL-Syntax

```sql
YEARS_SUB(<date>, <n>)
```

## SQL-Beispiele

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
