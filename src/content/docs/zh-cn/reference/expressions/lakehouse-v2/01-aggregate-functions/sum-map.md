---
title: SUM_MAP (Lakehouse v2)
description: SUM_MAP：按映射列中的键对值分组求和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum-map.md
---

按映射列中的键对值分组求和。

## Analyze 语法

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Analyze 示例

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQL 语法

```sql
SUM_MAP(<key_col>, <val_col>)
```

## SQL 示例

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
