---
title: VARIANT_GET (Lakehouse v2)
description: VARIANT_GET — Extrae un valor con tipo de un objeto VARIANT en una ruta especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-get.md
---

Extrae un valor con tipo de un objeto VARIANT en una ruta especificada.

## Sintaxis de Analyze

```python
func.variant_get(<variant>, <path>, <type>)
```

## Ejemplos de Analyze

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## Sintaxis de SQL

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## Ejemplos de SQL

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
