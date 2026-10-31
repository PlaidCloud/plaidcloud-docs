---
title: VARIANT_QUERY (Lakehouse v2)
description: "Use la función de variante VARIANT_QUERY en PlaidCloud Lakehouse. Consulta un valor de un objeto VARIANT mediante una expresión de ruta y devuelve un VARIANT."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

Consulta un valor de un objeto VARIANT mediante una expresión de ruta y devuelve un VARIANT.

## Sintaxis de Analyze

```python
func.variant_query(<variant>, <path>)
```

## Ejemplos de Analyze

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
VARIANT_QUERY(<variant>, <path>)
```

## Ejemplos de SQL

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
