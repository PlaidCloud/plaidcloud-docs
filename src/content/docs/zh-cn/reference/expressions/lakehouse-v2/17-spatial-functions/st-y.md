---
title: ST_Y (Lakehouse v2)
description: ST_Y：返回点几何对象的 Y 坐标（纬度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-y.md
---

返回点几何对象的 Y 坐标（纬度）。

## Analyze 语法

```python
func.st_y(<point>)
```

## Analyze 示例

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## SQL 语法

```sql
ST_Y(<point>)
```

## SQL 示例

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
