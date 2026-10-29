---
title: MAP_KEYS (Lakehouse v2)
description: MAP_KEYS — 以数组形式返回映射中的所有键。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-keys.md
---

以数组形式返回映射中的所有键。

## Analyze 语法

```python
func.map_keys(get_column(table, 'map_col'))
```

## Analyze 示例

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## SQL 语法

```sql
MAP_KEYS(<map_col>)
```

## SQL 示例

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
