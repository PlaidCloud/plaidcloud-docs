---
title: TO_UINT32 (Lakehouse v1)
description: TO_UINT32 – wandelt einen Wert in den Datentyp UINT32 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint32.md
---

Wandelt einen Wert in den Datentyp UINT32 um.

## Analyze-Syntax

```python
func.to_uint32( <expr> )
```

## Analyze-Beispiele

```python
func.to_uint32('123')

┌───────────────────────┐
│ func.to_uint32('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL-Syntax

```sql
TO_UINT32( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_UINT32('123');

┌──────────────────┐
│ to_uint32('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
