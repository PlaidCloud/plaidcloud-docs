---
title: DAYOFWEEK (Lakehouse v2)
description: DAYOFWEEK – gibt den Wochentagsindex für ein Datum zurück (1 = Sonntag, 7 = Samstag).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek.md
---

Gibt den Wochentagsindex für ein Datum zurück (1 = Sonntag, 7 = Samstag).

## Analyze-Syntax

```python
func.dayofweek(<date>)
```

## Analyze-Beispiele

```python
func.dayofweek('2024-06-15')

┌───┐
│ 7  │
└───┘
```

## SQL-Syntax

```sql
DAYOFWEEK(<date>)
```

## SQL-Beispiele

```sql
SELECT DAYOFWEEK('2024-06-15');

┌───┐
│ 7  │
└───┘
```
