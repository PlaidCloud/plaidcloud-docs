---
title: COLUMN_COMPRESSED_SIZE (Lakehouse v2)
description: COLUMN_COMPRESSED_SIZE — Devuelve el tamaño comprimido, en bytes, del valor de una columna.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-compressed-size.md
---

Devuelve el tamaño comprimido, en bytes, del valor de una columna.

## Sintaxis de Analyze

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Ejemplos de Analyze

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## Sintaxis de SQL

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## Ejemplos de SQL

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```
