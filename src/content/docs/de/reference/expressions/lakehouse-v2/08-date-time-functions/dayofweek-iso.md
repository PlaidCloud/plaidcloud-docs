---
title: DAYOFWEEK_ISO (Lakehouse v2)
description: DAYOFWEEK_ISO – gibt den ISO-Wochentagsindex für ein Datum zurück (1 = Montag, 7 = Sonntag).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek-iso.md
---

Gibt den ISO-Wochentagsindex für ein Datum zurück (1 = Montag, 7 = Sonntag).

## Analyze-Syntax

```python
func.dayofweek_iso(<date>)
```

## Analyze-Beispiele

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQL-Syntax

```sql
DAYOFWEEK_ISO(<date>)
```

## SQL-Beispiele

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```
