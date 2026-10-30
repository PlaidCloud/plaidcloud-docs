---
title: H3_HEX_AREA_KM2（Lakehouse v1）
description: H3_HEX_AREA_KM2 — 指定した解像度での六角形の平均面積を平方キロメートルで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-km2.md
---

指定した解像度での六角形の平均面積を平方キロメートルで返します。五角形は含まれません。

## Analyze Syntax

```python
func.h3_area_km2(res)
```

## Analyze Examples

```python
func.h3_area_km2(1)

┌─────────────────────────┐
│ func.h3_hex_area_km2(1) │
├─────────────────────────┤
│       609788.4417941332 │
└─────────────────────────┘
```

## SQL Syntax

```sql
H3_HEX_AREA_KM2(res)
```

## SQL Examples

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```
