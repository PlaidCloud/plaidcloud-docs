---
title: VARIANT_TYPEOF (Lakehouse v2)
description: VARIANT_TYPEOF — Devuelve el nombre del tipo de un valor VARIANT como una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-typeof.md
---

Devuelve el nombre del tipo de un valor VARIANT como una cadena.

## Sintaxis de Analyze

```python
func.variant_typeof(<variant>)
```

## Ejemplos de Analyze

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## Sintaxis de SQL

```sql
VARIANT_TYPEOF(<variant>)
```

## Ejemplos de SQL

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
