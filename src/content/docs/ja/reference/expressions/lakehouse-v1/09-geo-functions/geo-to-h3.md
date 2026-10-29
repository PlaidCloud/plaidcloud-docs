---
title: GEO_TO_H3（Lakehouse v1）
description: GEO_TO_H3 — 指定した位置が属する六角形セルのH3インデックスを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

指定した位置が属する六角形セルの[H3](https://eng.uber.com/h3/)インデックスを返します。0が返された場合は、エラーが発生したことを示します。

## Analyze Syntax

```python
func.geo_to_h3(lon, lat, res)
```

## Analyze Examples

```python
func.geo_to_h3(37.79506683, 55.71290588, 15)

┌──────────────────────────────────────────────┐
│ func.geo_to_h3(37.79506683, 55.71290588, 15) │
├──────────────────────────────────────────────┤
│                           644325524701193974 │
└──────────────────────────────────────────────┘
```

## SQL Syntax

```sql
GEO_TO_H3(lon, lat, res)
```

## SQL Examples

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```
