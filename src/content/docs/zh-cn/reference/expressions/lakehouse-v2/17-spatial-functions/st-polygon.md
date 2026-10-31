---
title: ST_POLYGON (Lakehouse v2)
description: ST_POLYGON：根据 WKT 字符串创建多边形几何对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-polygon.md
---

根据 WKT 字符串创建多边形几何对象。

## Analyze 语法

```python
func.st_polygon(<wkt>)
```

## Analyze 示例

```python
func.st_polygon('POLYGON((0 0,10 0,10 10,0 10,0 0))')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 语法

```sql
ST_POLYGON(<wkt>)
```

## SQL 示例

```sql
SELECT ST_ASTEXT(ST_POLYGON('POLYGON((0 0,10 0,10 10,0 10,0 0))'));

┌─────────────────────────────────────────┐
│ POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))  │
└─────────────────────────────────────────┘
```
