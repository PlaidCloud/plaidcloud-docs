---
title: TO_QUARTER (Lakehouse v1)
description: TO_QUARTER – ruft das Quartal (1, 2, 3 oder 4) aus einem angegebenen Datum oder Zeitstempel ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-quarter.md
---

Ruft das Quartal (1, 2, 3 oder 4) aus einem angegebenen Datum oder Zeitstempel ab.

## Analyze-Syntax

```python
func.to_quarter(<expr>)
```

## Analyze-Beispiele

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_QUARTER( <date_or_time_expr> )
```

## Aliase

- [QUARTER](../quarter)

## Rückgabetyp

Ganzzahl.

## SQL-Beispiele

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```
