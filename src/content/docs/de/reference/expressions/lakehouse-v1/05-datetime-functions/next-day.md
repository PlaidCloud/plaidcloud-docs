---
title: NEXT_DAY (Lakehouse v1)
description: NEXT_DAY – gibt das Datum des nächsten angegebenen Wochentags nach dem angegebenen Datum oder Zeitstempel zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/next-day.md
---

Gibt das Datum des nächsten angegebenen Wochentags nach dem angegebenen Datum oder Zeitstempel zurück.

## Analyze-Syntax

```python
func.next_day(date_expression>, <target_day>)
```

## Analyze-Beispiele

```python
func.next_day(func.to_date('2024-11-13'), 'monday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'monday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-18                                           │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
NEXT_DAY(<date_expression>, <target_day>)
```

| Parameter           | Beschreibung                                                                                                                                                             |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Ein `DATE`- oder `TIMESTAMP`-Wert, für den das nächste Auftreten des angegebenen Tages berechnet wird.                                                               |
| `<target_day>`      | Der Wochentag, dessen nächstes Auftreten gesucht wird. Zulässige Werte sind `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` und `sunday`. |

## Rückgabetyp

Datum.

## SQL-Beispiele

So finden Sie den nächsten Montag nach einem bestimmten Datum, etwa 2024-11-13:

```sql
SELECT NEXT_DAY(to_date('2024-11-13'), monday) AS next_monday;

┌─────────────┐
│ next_monday │
├─────────────┤
│ 2024-11-18  │
└─────────────┘
```
