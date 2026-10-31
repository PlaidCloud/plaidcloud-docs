---
title: MAP_APPLY (Lakehouse v2)
description: MAP_APPLY — 对映射中的每个键值对应用 lambda 表达式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-apply.md
---

对映射中的每个键值对应用 lambda 表达式。

## Analyze 语法

```python
func.map_apply(get_column(table, 'map_col'), lambda k, v: (k, v*2))
```

## Analyze 示例

```python
func.map_apply(MAP{'a':1,'b':2}, lambda k,v: (k, v*2))

┌───────────────┐
│ {'a':2,'b':4} │
└───────────────┘
```

## SQL 语法

```sql
MAP_APPLY(<map_col>, lambda k, v: (k, v*2))
```

## SQL 示例

```sql
SELECT MAP_APPLY((k, v) -> (k, v * 2), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"a":2,"b":4} │
└───────────────┘
```
