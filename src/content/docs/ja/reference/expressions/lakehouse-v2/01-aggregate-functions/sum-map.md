---
title: SUM_MAP (Lakehouse v2)
description: SUM_MAP — マップ列のキーごとに値を合計します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum-map.md
---

マップ列のキーごとに値を合計します。

## Analyzeの構文

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Analyzeの例

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQLの構文

```sql
SUM_MAP(<key_col>, <val_col>)
```

## SQLの例

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
