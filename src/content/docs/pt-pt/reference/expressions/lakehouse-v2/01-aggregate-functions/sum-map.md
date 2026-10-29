---
title: SUM_MAP (Lakehouse v2)
description: SUM_MAP — soma valores agrupados por chaves em colunas de mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum-map.md
---

Soma valores agrupados por chaves em colunas de mapa.

## Sintaxe do Analyze

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Exemplos do Analyze

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## Sintaxe SQL

```sql
SUM_MAP(<key_col>, <val_col>)
```

## Exemplos SQL

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
