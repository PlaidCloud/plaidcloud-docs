---
title: TO_BITMAP (Lakehouse v1)
description: TO_BITMAP — convierte un valor al tipo de datos BITMAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-bitmap.md
---

Convierte un valor al tipo de datos BITMAP.

## Sintaxis de Analyze

```python
func.to_bitmap( <expr> )
```

## Ejemplos de Analyze

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_BITMAP( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```
