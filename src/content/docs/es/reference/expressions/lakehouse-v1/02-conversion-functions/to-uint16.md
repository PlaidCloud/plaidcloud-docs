---
title: TO_UINT16 (Lakehouse v1)
description: TO_UINT16 — convierte un valor al tipo de datos UINT16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint16.md
---

Convierte un valor al tipo de datos UINT16.

## Sintaxis de Analyze

```python
func.to_uint16( <expr> )
```

## Ejemplos de Analyze

```python
func.to_uint16('123')

┌───────────────────────┐
│ func.to_uint16('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TO_UINT16( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_UINT16('123');

┌──────────────────┐
│ to_uint16('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
