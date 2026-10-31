---
title: TO_INT64 (Lakehouse v1)
description: TO_INT64 — convierte un valor al tipo de datos INT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int64.md
---

Convierte un valor al tipo de datos INT64.

## Sintaxis de Analyze

```python
func.to_int64( <expr> )
```

## Ejemplos de Analyze

```python
func.to_int64('123')

┌──────────────────────┐
│ func.to_int64('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
TO_INT64( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_INT64('123');

┌─────────────────┐
│ to_int64('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
