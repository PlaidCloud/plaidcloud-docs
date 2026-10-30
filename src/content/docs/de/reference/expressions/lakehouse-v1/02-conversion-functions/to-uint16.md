---
title: TO_UINT16 (Lakehouse v1)
description: TO_UINT16 – wandelt einen Wert in den Datentyp UINT16 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint16.md
---

Wandelt einen Wert in den Datentyp UINT16 um.

## Analyze-Syntax

```python
func.to_uint16( <expr> )
```

## Analyze-Beispiele

```python
func.to_uint16('123')

┌───────────────────────┐
│ func.to_uint16('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL-Syntax

```sql
TO_UINT16( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_UINT16('123');

┌──────────────────┐
│ to_uint16('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
