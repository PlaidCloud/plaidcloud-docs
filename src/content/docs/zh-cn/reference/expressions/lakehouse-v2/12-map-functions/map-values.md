---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES — 以数组形式返回映射中的所有值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-values.md
---

以数组形式返回映射中的所有值。

## Analyze 语法

```python
func.map_values(get_column(table, 'map_col'))
```

## Analyze 示例

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## SQL 语法

```sql
MAP_VALUES(<map_col>)
```

## SQL 示例

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
