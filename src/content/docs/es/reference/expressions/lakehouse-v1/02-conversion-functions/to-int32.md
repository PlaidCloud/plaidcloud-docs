---
title: TO_INT32 (Lakehouse v1)
description: TO_INT32 — convierte un valor al tipo de datos INT32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int32.md
---

Convierte un valor al tipo de datos INT32.

## Sintaxis de Analyze

```python
func.to_int32( <expr> )
```

## Ejemplos de Analyze

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
TO_INT32( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
