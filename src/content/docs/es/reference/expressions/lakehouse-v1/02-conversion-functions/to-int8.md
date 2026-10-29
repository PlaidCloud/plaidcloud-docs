---
title: TO_INT8 (Lakehouse v1)
description: TO_INT8 — convierte un valor al tipo de datos INT8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int8.md
---

Convierte un valor al tipo de datos INT8.

## Sintaxis de Analyze

```python
func.to_int8( <expr> )
```

## Ejemplos de Analyze

```python
func.to_int8('123')

┌─────────────────────┐
│ func.to_int8('123') │
├─────────────────────┤
│                 123 │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
TO_INT8( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```
