---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE — 根据圆心经度、纬度和以米为单位的半径创建圆形几何对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-circle.md
---

根据圆心经度、纬度和以米为单位的半径创建圆形几何对象。

## Analyze 语法

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Analyze 示例

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 语法

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## SQL 示例

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
