---
title: DATE_SLICE (Lakehouse v2)
description: "Verwenden Sie die Datums-/Zeitfunktion DATE_SLICE in PlaidCloud Lakehouse. Rechnet eine angegebene Zeit anhand des festgelegten Zeitraums auf den Anfang oder das Ende eines Zeitintervalls um."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-slice.md
---

Rechnet eine angegebene Zeit anhand des festgelegten Zeitraums auf den Anfang oder das Ende eines Zeitintervalls um.

## Analyze-Syntax

```python
func.date_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyze-Beispiele

```python
func.date_slice('2024-06-15 14:35:00', text('INTERVAL 1 HOUR'))

┌───────────────────────┐
│ '2024-06-15 14:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
DATE_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQL-Beispiele

```sql
SELECT DATE_SLICE('2024-06-15 14:35:00', INTERVAL 1 HOUR);

┌─────────────────────┐
│ 2024-06-15 14:00:00  │
└─────────────────────┘
```
