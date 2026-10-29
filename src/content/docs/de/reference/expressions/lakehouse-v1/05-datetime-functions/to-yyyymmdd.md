---
title: TO_YYYYMMDD (Lakehouse v1)
description: TO_YYYYMMDD – wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt32-Zahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmdd.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt32-Zahl um, die Jahr, Monat und Tag enthält (YYYY * 10000 + MM * 100 + DD).

## Analyze-Syntax

```python
func.to_yyyymmdd(<expr>)
```

## Analyze-Beispiele

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_YYYYMMDD(<expr>)
```

## Argumente

| Argumente | Beschreibung  |
|-----------|---------------|
| `<expr>`  | Datum/Datetime |

## Rückgabetyp

`INT`, gibt den Wert im Format `YYYYMMDD` zurück.

## SQL-Beispiele

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```
