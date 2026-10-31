---
title: TO_UINT32 (Lakehouse v1)
description: TO_UINT32 — convierte un valor al tipo de datos UINT32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint32.md
---

Convierte un valor al tipo de datos UINT32.

## Sintaxis de Analyze

```python
func.to_uint32( <expr> )
```

## Ejemplos de Analyze

```python
func.to_uint32('123')

┌───────────────────────┐
│ func.to_uint32('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TO_UINT32( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_UINT32('123');

┌──────────────────┐
│ to_uint32('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
