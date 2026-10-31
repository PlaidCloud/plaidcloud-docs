---
title: ADDDATE (Lakehouse v2)
description: ADDDATE – addiert ein angegebenes Zeitintervall zu einem Datum. Alias für `DATE_ADD`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/adddate.md
---

Addiert ein angegebenes Zeitintervall zu einem Datum. Alias für `DATE_ADD`.

## Analyze-Syntax

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Analyze-Beispiele

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQL-Syntax

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## SQL-Beispiele

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
