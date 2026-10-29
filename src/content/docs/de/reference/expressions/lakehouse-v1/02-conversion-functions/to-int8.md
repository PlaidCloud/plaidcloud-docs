---
title: TO_INT8 (Lakehouse v1)
description: TO_INT8 – wandelt einen Wert in den Datentyp INT8 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int8.md
---

Wandelt einen Wert in den Datentyp INT8 um.

## Analyze-Syntax

```python
func.to_int8( <expr> )
```

## Analyze-Beispiele

```python
func.to_int8('123')

┌─────────────────────┐
│ func.to_int8('123') │
├─────────────────────┤
│                 123 │
└─────────────────────┘
```

## SQL-Syntax

```sql
TO_INT8( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```
