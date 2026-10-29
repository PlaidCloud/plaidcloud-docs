---
title: "CARDINALITY (Map, Lakehouse v2)"
description: CARDINALITY — 返回映射中键值对的数量。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

返回映射中键值对的数量。

## Analyze 语法

```python
func.cardinality(get_column(table, 'map_col'))
```

## Analyze 示例

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQL 语法

```sql
CARDINALITY(<map_col>)
```

## SQL 示例

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
