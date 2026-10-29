---
title: MAP_FILTER (Lakehouse v2)
description: MAP_FILTER — 使用 lambda 表达式筛选映射中的键值对。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-filter.md
---

使用 lambda 表达式筛选映射中的键值对。

## Analyze 语法

```python
func.map_filter(get_column(table, 'map_col'), lambda k, v: v > 1)
```

## Analyze 示例

```python
func.map_filter(MAP{'a':1,'b':2,'c':3}, lambda k,v: v>1)

┌───────────────┐
│ {'b':2,'c':3} │
└───────────────┘
```

## SQL 语法

```sql
MAP_FILTER(<map_col>, lambda k, v: v > 1)
```

## SQL 示例

```sql
SELECT MAP_FILTER((k, v) -> v > 1, MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ {"b":2,"c":3} │
└───────────────┘
```
