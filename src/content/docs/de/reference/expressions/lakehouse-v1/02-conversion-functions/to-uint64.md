---
title: TO_UINT64 (Lakehouse v1)
description: TO_UINT64 – wandelt einen Wert in den Datentyp UINT64 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint64.md
---

Wandelt einen Wert in den Datentyp UINT64 um.

## Analyze-Syntax

```python
func.to_uint64( <expr> )
```

## Analyze-Beispiele

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL-Syntax

```sql
TO_UINT64( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
