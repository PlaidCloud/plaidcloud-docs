---
title: TO_INT16 (Lakehouse v1)
description: TO_INT16 — convierte un valor al tipo de datos INT16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int16.md
---

Convierte un valor al tipo de datos INT16.

## Sintaxis de Analyze

```python
func.to_int16( <expr> )
```

## Ejemplos de Analyze

```python
func.to_int16('123')

┌──────────────────────┐
│ func.to_int16('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
TO_INT16( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_INT16('123');

┌─────────────────┐
│ to_int16('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
