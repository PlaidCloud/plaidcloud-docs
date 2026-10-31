---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT — 将多个映射合并为一个映射。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

将多个映射合并为一个映射。

## Analyze 语法

```python
func.map_concat(map1, map2)
```

## Analyze 示例

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## SQL 语法

```sql
MAP_CONCAT(map1, map2)
```

## SQL 示例

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
