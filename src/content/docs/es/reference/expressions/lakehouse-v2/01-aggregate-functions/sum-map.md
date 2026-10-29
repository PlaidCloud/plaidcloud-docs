---
title: SUM_MAP (Lakehouse v2)
description: SUM_MAP — suma valores agrupados por claves en columnas de tipo mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum-map.md
---

Suma valores agrupados por claves en columnas de tipo mapa.

## Sintaxis de Analyze

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Ejemplos de Analyze

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## Sintaxis de SQL

```sql
SUM_MAP(<key_col>, <val_col>)
```

## Ejemplos de SQL

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
