---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE — 返回映射中键值对的数量。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

返回映射中键值对的数量。

## Analyze 语法

```python
func.map_size(get_column(table, 'map_col'))
```

## Analyze 示例

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQL 语法

```sql
MAP_SIZE(<map_col>)
```

## SQL 示例

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
