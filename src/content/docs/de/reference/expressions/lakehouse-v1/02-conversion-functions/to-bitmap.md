---
title: TO_BITMAP (Lakehouse v1)
description: TO_BITMAP – wandelt einen Wert in den Datentyp BITMAP um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-bitmap.md
---

Wandelt einen Wert in den Datentyp BITMAP um.

## Analyze-Syntax

```python
func.to_bitmap( <expr> )
```

## Analyze-Beispiele

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## SQL-Syntax

```sql
TO_BITMAP( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```
