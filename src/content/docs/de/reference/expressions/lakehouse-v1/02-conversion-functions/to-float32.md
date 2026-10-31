---
title: TO_FLOAT32 (Lakehouse v1)
description: TO_FLOAT32 – wandelt einen Wert in den Datentyp FLOAT32 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float32.md
---

Wandelt einen Wert in den Datentyp FLOAT32 um.

## Analyze-Syntax

```python
func.to_float32( <expr> )
```

## Analyze-Beispiele

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL-Syntax

```sql
TO_FLOAT32( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
