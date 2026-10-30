---
title: SPLIT_PART (Lakehouse v2)
description: SPLIT_PART — Divide una cadena por un delimitador y devuelve el elemento en un índice especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

Divide una cadena por un delimitador y devuelve el elemento en un índice especificado.

## Sintaxis de Analyze

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Ejemplos de Analyze

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## Sintaxis de SQL

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## Ejemplos de SQL

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
