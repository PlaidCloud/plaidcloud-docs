---
title: ST_POINT (Lakehouse v2)
description: ST_POINT：根据经度和纬度值创建点几何对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-point.md
---

根据经度和纬度值创建点几何对象。

## Analyze 语法

```python
func.st_point(<lng>, <lat>)
```

## Analyze 示例

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 语法

```sql
ST_POINT(<lng>, <lat>)
```

## SQL 示例

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
