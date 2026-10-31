---
title: TO_FLOAT64 (Lakehouse v1)
description: TO_FLOAT64 — convierte un valor al tipo de datos FLOAT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float64.md
---

Convierte un valor al tipo de datos FLOAT64.

## Sintaxis de Analyze

```python
func.to_float64( <expr> )
```

## Ejemplos de Analyze

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_FLOAT64( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
