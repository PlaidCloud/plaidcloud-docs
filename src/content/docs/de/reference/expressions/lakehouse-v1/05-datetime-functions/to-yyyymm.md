---
title: TO_YYYYMM (Lakehouse v1)
description: TO_YYYYMM – wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt32-Zahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymm.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt32-Zahl um, die Jahr und Monat enthält.

## Analyze-Syntax

```python
func.to_yyyymm(<expr>)
```

## Analyze-Beispiele

```python
func.to_yyyymm('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_yyyymm('2023-11-12 09:38:18.165575') │
│                   UInt32                     │
├──────────────────────────────────────────────┤
│                                       202311 │
└──────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_YYYYMM(<expr>)
```

## Argumente

| Argumente | Beschreibung   |
|-----------|----------------|
| `<expr>`  | Datum/Timestamp |

## Rückgabetyp

`INT`, gibt den Wert im Format `YYYYMM` zurück.

## SQL-Beispiele

```sql
SELECT
  to_yyyymm('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_yyyymm('2023-11-12 09:38:18.165575') │
│                  UInt32                 │
├─────────────────────────────────────────┤
│                                  202311 │
└─────────────────────────────────────────┘
```
