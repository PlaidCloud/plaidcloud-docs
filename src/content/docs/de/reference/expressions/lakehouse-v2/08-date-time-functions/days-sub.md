---
title: DAYS_SUB (Lakehouse v2)
description: DAYS_SUB – subtrahiert eine angegebene Anzahl von Tagen von einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-sub.md
---

Subtrahiert eine angegebene Anzahl von Tagen von einem Datum.

## Analyze-Syntax

```python
func.days_sub(<date>, <n>)
```

## Analyze-Beispiele

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL-Syntax

```sql
DAYS_SUB(<date>, <n>)
```

## SQL-Beispiele

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
