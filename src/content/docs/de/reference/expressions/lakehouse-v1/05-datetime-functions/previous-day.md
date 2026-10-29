---
title: PREVIOUS_DAY (Lakehouse v1)
description: PREVIOUS_DAY – gibt das Datum des letzten angegebenen Wochentags vor dem angegebenen Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/previous-day.md
---

Gibt das Datum des letzten angegebenen Wochentags vor dem angegebenen Datum oder Zeitstempel zurück.

## Analyze-Syntax

```python
func.next_day(date_expression>, <target_day>)
```

## Analyze-Beispiele

```python
func.next_day(func.to_date('2024-11-13'), 'friday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'friday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-08                                           │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
PREVIOUS_DAY(<date_expression>, <target_day>)
```

| Parameter           | Beschreibung                                                                                                                                                             |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Ein `DATE`- oder `TIMESTAMP`-Wert, für den das vorherige Auftreten des angegebenen Tages berechnet wird.                                                             |
| `<target_day>`      | Der Wochentag, dessen vorheriges Auftreten gesucht wird. Zulässige Werte sind `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` und `sunday`.  |

## Rückgabetyp

Datum.

## SQL-Beispiele

So finden Sie den letzten Freitag vor einem bestimmten Datum, etwa 2024-11-13:

```sql
SELECT PREVIOUS_DAY(to_date('2024-11-13'), friday) AS last_friday;

┌─────────────┐
│ last_friday │
├─────────────┤
│ 2024-11-08  │
└─────────────┘
```
