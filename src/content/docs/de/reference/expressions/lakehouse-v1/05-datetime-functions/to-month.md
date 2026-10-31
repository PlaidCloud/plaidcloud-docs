---
title: TO_MONTH (Lakehouse v1)
description: TO_MONTH – wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die die Monatsnummer enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-month.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die die Monatsnummer (1–12) enthält.

## Analyze-Syntax

```python
func.to_month(<expr>)
```

## Analyze-Beispiele

```python
func.now(), func.to_month(func.now()), func.month(func.now())

┌─────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_month(func.now()) │ func.month(func.now()) │
├────────────────────────────┼───────────────────────────┼────────────────────────┤
│ 2024-03-14 23:34:02.161291 │                         3 │                      3 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_MONTH(<expr>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------|-------------------|
| `<expr>`  | Datum/Zeitstempel |

## Aliase

- [MONTH](../month)

## Rückgabetyp

 `TINYINT`

## SQL-Beispiele

```sql
SELECT NOW(), TO_MONTH(NOW()), MONTH(NOW());

┌─────────────────────────────────────────────────────────────┐
│            now()           │ to_month(now()) │ month(now()) │
├────────────────────────────┼─────────────────┼──────────────┤
│ 2024-03-14 23:34:02.161291 │               3 │            3 │
└─────────────────────────────────────────────────────────────┘
```
