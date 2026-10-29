---
title: SUM_MAP (Lakehouse v2)
description: SUM_MAP – summiert Werte, gruppiert nach den Schlüsseln in Map-Spalten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum-map.md
---

Summiert Werte, gruppiert nach den Schlüsseln in Map-Spalten.

## Analyze-Syntax

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Analyze-Beispiele

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQL-Syntax

```sql
SUM_MAP(<key_col>, <val_col>)
```

## SQL-Beispiele

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
