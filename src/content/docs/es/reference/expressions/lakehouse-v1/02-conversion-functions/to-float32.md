---
title: TO_FLOAT32 (Lakehouse v1)
description: TO_FLOAT32 — convierte un valor al tipo de datos FLOAT32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float32.md
---

Convierte un valor al tipo de datos FLOAT32.

## Sintaxis de Analyze

```python
func.to_float32( <expr> )
```

## Ejemplos de Analyze

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_FLOAT32( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
