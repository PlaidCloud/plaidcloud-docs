---
title: ST_X (Lakehouse v2)
description: ST_X：返回点几何对象的 X 坐标（经度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-x.md
---

返回点几何对象的 X 坐标（经度）。

## Analyze 语法

```python
func.st_x(<point>)
```

## Analyze 示例

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## SQL 语法

```sql
ST_X(<point>)
```

## SQL 示例

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
