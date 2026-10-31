---
title: "ELEMENT_AT (Map, Lakehouse v2)"
description: ELEMENT_AT — 返回映射中与指定键关联的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

返回映射中与指定键关联的值。

## Analyze 语法

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Analyze 示例

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## SQL 语法

```sql
ELEMENT_AT(<map_col>, 'key')
```

## SQL 示例

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
