---
title: DAYNAME (Lakehouse v2)
description: DAYNAME – gibt den Namen des Wochentags für ein Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayname.md
---

Gibt den Namen des Wochentags für ein Datum zurück.

## Analyze-Syntax

```python
func.dayname(<date>)
```

## Analyze-Beispiele

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## SQL-Syntax

```sql
DAYNAME(<date>)
```

## SQL-Beispiele

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```
