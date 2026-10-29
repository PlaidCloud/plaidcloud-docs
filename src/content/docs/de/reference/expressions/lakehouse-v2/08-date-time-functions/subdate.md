---
title: SUBDATE (Lakehouse v2)
description: SUBDATE – subtrahiert ein Zeitintervall von einem Datum. Alias für `DATE_SUB`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/subdate.md
---

Subtrahiert ein Zeitintervall von einem Datum. Alias für `DATE_SUB`.

## Analyze-Syntax

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Analyze-Beispiele

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## SQL-Syntax

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## SQL-Beispiele

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```
