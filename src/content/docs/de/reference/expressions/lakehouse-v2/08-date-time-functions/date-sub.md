---
title: DATE_SUB (Lakehouse v2)
description: DATE_SUB – subtrahiert ein angegebenes Zeitintervall von einem Datum oder Datums-/Zeitwert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-sub.md
---

Subtrahiert ein angegebenes Zeitintervall von einem Datum oder Datums-/Zeitwert.

## Analyze-Syntax

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Analyze-Beispiele

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## SQL-Syntax

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## SQL-Beispiele

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```
