---
title: TO_YEAR (Lakehouse v1)
description: TO_YEAR – wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt16-Zahl mit der Jahreszahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-year.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt16-Zahl um, die die Jahreszahl (n. Chr.) enthält.

## Analyze-Syntax

```python
func.to_year(<expr>)
```

## Analyze-Beispiele

```python
func.now(), func.to_year(func.now()), func.year(func.now())

┌───────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_year(func.now()) │ func.year(func.now()) │
├────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 2024-03-14 23:37:03.895166 │                     2024 │                  2024 │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_YEAR(<expr>)
```

## Argumente

| Argumente | Beschreibung   |
|-----------|----------------|
| `<expr>`  | Datum/Timestamp |

## Aliase

- [YEAR](../year)

## Rückgabetyp

 `SMALLINT`

## SQL-Beispiele

```sql
SELECT NOW(), TO_YEAR(NOW()), YEAR(NOW());

┌───────────────────────────────────────────────────────────┐
│            now()           │ to_year(now()) │ year(now()) │
├────────────────────────────┼────────────────┼─────────────┤
│ 2024-03-14 23:37:03.895166 │           2024 │        2024 │
└───────────────────────────────────────────────────────────┘
```
