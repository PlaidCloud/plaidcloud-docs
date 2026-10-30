---
title: TO_WEEK_OF_YEAR (Lakehouse v1)
description: TO_WEEK_OF_YEAR – berechnet die Kalenderwoche innerhalb eines Jahres für ein angegebenes Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-week-of-year.md
---

Berechnet die Kalenderwoche innerhalb eines Jahres für ein angegebenes Datum.

Die ISO-Wochennummerierung funktioniert wie folgt: Der 4. Januar gehört immer zur ersten Woche. Fällt der 1. Januar auf einen Donnerstag, ist die Woche vom Montag, 29. Dezember, bis zum Sonntag, 4. Januar, die ISO-Woche 1. Fällt der 1. Januar auf einen Freitag, ist die Woche vom Montag, 4. Januar, bis zum Sonntag, 10. Januar, die ISO-Woche 1.

## Analyze-Syntax

```python
func.to_week_of_year(<expr>)
```

## Analyze-Beispiele

```python
func.now(), func.to_week_of_year(func.now()), func.week(func.now()), func.weekofyear(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_week_of_year(func.now()) │ func.week(func.now()) │ func.weekofyear(func.now()) │
├────────────────────────────┼──────────────────────────────────┼───────────────────────┼─────────────────────────────┤
│ 2024-03-14 23:30:04.011624 │                               11 │                    11 │                          11 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_WEEK_OF_YEAR(<expr>)
```

## Argumente

| Argumente | Beschreibung   |
|-----------|----------------|
| `<expr>`  | Datum/Timestamp |

## Aliase

- [WEEK](../week)
- [WEEKOFYEAR](../weekofyear)

## Rückgabetyp

Gibt eine Ganzzahl zurück, die die Kalenderwoche innerhalb eines Jahres angibt, mit einer Nummerierung von 1 bis 53.

## SQL-Beispiele

```sql
SELECT NOW(), TO_WEEK_OF_YEAR(NOW()), WEEK(NOW()), WEEKOFYEAR(NOW());

┌───────────────────────────────────────────────────────────────────────────────────────┐
│            now()           │ to_week_of_year(now()) │ week(now()) │ weekofyear(now()) │
├────────────────────────────┼────────────────────────┼─────────────┼───────────────────┤
│ 2024-03-14 23:30:04.011624 │                     11 │          11 │                11 │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
