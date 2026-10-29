---
title: SUM_MAP (Lakehouse v2)
description: SUM_MAP — additionne les valeurs regroupées par clés dans des colonnes de type map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum-map.md
---

Additionne les valeurs regroupées par clés dans des colonnes de type map.

## Syntaxe Analyze

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Exemples Analyze

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## Syntaxe SQL

```sql
SUM_MAP(<key_col>, <val_col>)
```

## Exemples SQL

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
