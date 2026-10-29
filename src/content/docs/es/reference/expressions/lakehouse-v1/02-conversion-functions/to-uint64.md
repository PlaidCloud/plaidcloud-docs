---
title: TO_UINT64 (Lakehouse v1)
description: TO_UINT64 — convierte un valor al tipo de datos UINT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint64.md
---

Convierte un valor al tipo de datos UINT64.

## Sintaxis de Analyze

```python
func.to_uint64( <expr> )
```

## Ejemplos de Analyze

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TO_UINT64( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
