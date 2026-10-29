---
title: TO_VARIANT (Lakehouse v1)
description: TO_VARIANT – wandelt einen Wert in den Datentyp VARIANT um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-variant.md
---

Wandelt einen Wert in den Datentyp VARIANT um.

## Analyze-Syntax

```python
func.to_variant( <expr> )
```

## Analyze-Beispiele

```python
func.to_variant(to_bitmap('100,200,300'))

┌───────────────────────────────────────────┐
│ func.to_variant(to_bitmap('100,200,300')) │
├───────────────────────────────────────────┤
│ [100,200,300]                             │
└───────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_VARIANT( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_VARIANT(TO_BITMAP('100,200,300'));

┌──────────────────────────────────────┐
│ to_variant(to_bitmap('100,200,300')) │
├──────────────────────────────────────┤
│ [100,200,300]                        │
└──────────────────────────────────────┘
```
