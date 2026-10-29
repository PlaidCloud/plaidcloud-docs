---
title: DISTINCT_MAP_KEYS (Lakehouse v2)
description: DISTINCT_MAP_KEYS — 返回映射中不重复的键。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/distinct-map-keys.md
---

返回映射中不重复的键。

## Analyze 语法

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Analyze 示例

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL 语法

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## SQL 示例

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
