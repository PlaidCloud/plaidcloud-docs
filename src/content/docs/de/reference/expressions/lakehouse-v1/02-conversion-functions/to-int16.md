---
title: TO_INT16 (Lakehouse v1)
description: TO_INT16 – wandelt einen Wert in den Datentyp INT16 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int16.md
---

Wandelt einen Wert in den Datentyp INT16 um.

## Analyze-Syntax

```python
func.to_int16( <expr> )
```

## Analyze-Beispiele

```python
func.to_int16('123')

┌──────────────────────┐
│ func.to_int16('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL-Syntax

```sql
TO_INT16( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_INT16('123');

┌─────────────────┐
│ to_int16('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
