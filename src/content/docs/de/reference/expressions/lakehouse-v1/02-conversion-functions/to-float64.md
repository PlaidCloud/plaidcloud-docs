---
title: TO_FLOAT64 (Lakehouse v1)
description: TO_FLOAT64 – wandelt einen Wert in den Datentyp FLOAT64 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float64.md
---

Wandelt einen Wert in den Datentyp FLOAT64 um.

## Analyze-Syntax

```python
func.to_float64( <expr> )
```

## Analyze-Beispiele

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL-Syntax

```sql
TO_FLOAT64( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
