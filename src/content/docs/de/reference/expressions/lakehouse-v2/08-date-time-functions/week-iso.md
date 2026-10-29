---
title: WEEK_ISO (Lakehouse v2)
description: WEEK_ISO – gibt die ISO-Kalenderwoche des Jahres für ein Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week-iso.md
---

Gibt die ISO-Kalenderwoche des Jahres für ein Datum zurück.

## Analyze-Syntax

```python
func.week_iso(<date>)
```

## Analyze-Beispiele

```python
func.week_iso('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL-Syntax

```sql
WEEK_ISO(<date>)
```

## SQL-Beispiele

```sql
SELECT WEEK_ISO('2024-06-15');

┌────┐
│ 24  │
└────┘
```
