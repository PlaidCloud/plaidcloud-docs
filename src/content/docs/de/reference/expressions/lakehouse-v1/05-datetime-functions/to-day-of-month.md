---
title: TO_DAY_OF_MONTH (Lakehouse v1)
description: TO_DAY_OF_MONTH – wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-month.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die den Tag des Monats (1–31) enthält.

## Analyze-Syntax

```python
func.to_day_of_month(<expr>)
```

## Analyze-Beispiele

```python
func.now(), func.to_day_of_month(func.now()), func.day(func.now())

┌──────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_day_of_month(func.now()) │ func.day(func.now()) │
├────────────────────────────┼──────────────────────────────────┼──────────────────────┤
│ 2024-03-14 23:35:41.947962 │                               14 │                   14 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_DAY_OF_MONTH(<expr>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------|-------------------|
| `<expr>`  | Datum/Zeitstempel |

## Aliase

- [DAY](../day)

## Rückgabetyp

`TINYINT`

## SQL-Beispiele

```sql
SELECT NOW(), TO_DAY_OF_MONTH(NOW()), DAY(NOW());

┌──────────────────────────────────────────────────────────────────┐
│            now()           │ to_day_of_month(now()) │ day(now()) │
├────────────────────────────┼────────────────────────┼────────────┤
│ 2024-03-14 23:35:41.947962 │                     14 │         14 │
└──────────────────────────────────────────────────────────────────┘
```
