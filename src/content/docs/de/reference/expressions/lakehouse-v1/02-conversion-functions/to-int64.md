---
title: TO_INT64 (Lakehouse v1)
description: TO_INT64 – wandelt einen Wert in den Datentyp INT64 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int64.md
---

Wandelt einen Wert in den Datentyp INT64 um.

## Analyze-Syntax

```python
func.to_int64( <expr> )
```

## Analyze-Beispiele

```python
func.to_int64('123')

┌──────────────────────┐
│ func.to_int64('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL-Syntax

```sql
TO_INT64( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_INT64('123');

┌─────────────────┐
│ to_int64('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
