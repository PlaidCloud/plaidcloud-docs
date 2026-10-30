---
title: TRANSFORM_VALUES (Lakehouse v2)
description: TRANSFORM_VALUES — 应用 lambda 表达式转换映射的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-values.md
---

应用 lambda 表达式转换映射的值。

## Analyze 语法

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Analyze 示例

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQL 语法

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## SQL 示例

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
