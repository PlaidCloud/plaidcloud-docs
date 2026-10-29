---
title: TO_UINT8 (Lakehouse v1)
description: TO_UINT8 – wandelt einen Wert in den Datentyp UINT8 um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint8.md
---

Wandelt einen Wert in den Datentyp UINT8 um.

## Analyze-Syntax

```python
func.to_uint8( <expr> )
```

## Analyze-Beispiele

```python
func.to_uint8('123')

┌──────────────────────┐
│ func.to_uint8('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL-Syntax

```sql
TO_UINT8( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_UINT8('123');

┌─────────────────┐
│ to_uint8('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
