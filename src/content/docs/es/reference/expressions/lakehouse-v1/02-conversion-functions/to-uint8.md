---
title: TO_UINT8 (Lakehouse v1)
description: TO_UINT8 — convierte un valor al tipo de datos UINT8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint8.md
---

Convierte un valor al tipo de datos UINT8.

## Sintaxis de Analyze

```python
func.to_uint8( <expr> )
```

## Ejemplos de Analyze

```python
func.to_uint8('123')

┌──────────────────────┐
│ func.to_uint8('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
TO_UINT8( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_UINT8('123');

┌─────────────────┐
│ to_uint8('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
