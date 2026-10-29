---
title: ST_CONTAINS (Lakehouse v2)
description: ST_CONTAINS — 检查一个几何对象是否包含另一个几何对象。为真时返回 1。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-contains.md
---

检查一个几何对象是否包含另一个几何对象。为真时返回 1。

## Analyze 语法

```python
func.st_contains(<geometry1>, <geometry2>)
```

## Analyze 示例

```python
func.st_contains(get_column(table, 'area'), func.st_point(1, 1))

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## SQL 示例

```sql
SELECT ST_CONTAINS(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_POINT(5, 5));

┌───┐
│ 1  │
└───┘
```
