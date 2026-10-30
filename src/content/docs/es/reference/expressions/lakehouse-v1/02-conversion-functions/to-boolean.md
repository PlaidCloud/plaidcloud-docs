---
title: TO_BOOLEAN (Lakehouse v1)
description: TO_BOOLEAN — convierte un valor al tipo de datos BOOLEAN.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-boolean.md
---

Convierte un valor al tipo de datos BOOLEAN.

## Sintaxis de Analyze

```python
func.to_boolean( <expr> )
```

## Ejemplos de Analyze

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_BOOLEAN( <expr> )
```

## Ejemplos de SQL

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```
