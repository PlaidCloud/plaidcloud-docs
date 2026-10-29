---
title: WEEKDAY (Lakehouse v2)
description: WEEKDAY – gibt den Wochentagsindex für ein Datum zurück (0 = Montag, 6 = Sonntag).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekday.md
---

Gibt den Wochentagsindex für ein Datum zurück (0 = Montag, 6 = Sonntag).

## Analyze-Syntax

```python
func.weekday(<date>)
```

## Analyze-Beispiele

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## SQL-Syntax

```sql
WEEKDAY(<date>)
```

## SQL-Beispiele

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```
