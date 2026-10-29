---
title: GEO_TO_H3（Lakehouse v1）
description: GEO_TO_H3 — 返回给定位置所在六边形单元的 H3 索引。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

返回给定位置所在六边形单元的 [H3](https://eng.uber.com/h3/) 索引。返回 0 表示发生了错误。

## Analyze 语法

```python
func.geo_to_h3(lon, lat, res)
```

## Analyze 示例

```python
func.geo_to_h3(37.79506683, 55.71290588, 15)

┌──────────────────────────────────────────────┐
│ func.geo_to_h3(37.79506683, 55.71290588, 15) │
├──────────────────────────────────────────────┤
│                           644325524701193974 │
└──────────────────────────────────────────────┘
```

## SQL 语法

```sql
GEO_TO_H3(lon, lat, res)
```

## SQL 示例

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```
