---
title: SPLIT (Lakehouse v2)
description: SPLIT — Divide una cadena por un delimitador y devuelve una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split.md
---

Divide una cadena por un delimitador y devuelve una matriz.

## Sintaxis de Analyze

```python
func.split(<str>, <delimiter>)
```

## Ejemplos de Analyze

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## Sintaxis de SQL

```sql
SPLIT(<str>, <delimiter>)
```

## Ejemplos de SQL

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
