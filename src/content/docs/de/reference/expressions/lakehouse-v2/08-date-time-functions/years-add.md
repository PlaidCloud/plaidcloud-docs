---
title: YEARS_ADD (Lakehouse v2)
description: YEARS_ADD – addiert eine angegebene Anzahl von Jahren zu einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-add.md
---

Addiert eine angegebene Anzahl von Jahren zu einem Datum.

## Analyze-Syntax

```python
func.years_add(<date>, <n>)
```

## Analyze-Beispiele

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## SQL-Syntax

```sql
YEARS_ADD(<date>, <n>)
```

## SQL-Beispiele

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```
