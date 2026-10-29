---
title: TO_INT32 (Lakehouse v1)
description: TO_INT32 – wandelt einen Wert in den Datentyp INT32 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int32.md
---

Wandelt einen Wert in den Datentyp INT32 um.

## Analyze-Syntax

```python
func.to_int32( <expr> )
```

## Analyze-Beispiele

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL-Syntax

```sql
TO_INT32( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
