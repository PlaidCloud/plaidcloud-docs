---
title: DATE_ADD (Lakehouse v2)
description: DATE_ADD – addiert ein angegebenes Zeitintervall zu einem Datum oder Datums-/Zeitwert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-add.md
---

Addiert ein angegebenes Zeitintervall zu einem Datum oder Datums-/Zeitwert.

## Analyze-Syntax

```python
func.date_add(<date>, INTERVAL <n> <unit>)
```

## Analyze-Beispiele

```python
func.date_add('2024-01-01', text('INTERVAL 30 DAY'))

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQL-Syntax

```sql
DATE_ADD(<date>, INTERVAL <n> <unit>)
```

## SQL-Beispiele

```sql
SELECT DATE_ADD('2024-01-01', INTERVAL 30 DAY);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
