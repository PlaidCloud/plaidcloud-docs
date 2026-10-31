---
title: H3_HEX_AREA_KM2（Lakehouse v1）
description: H3_HEX_AREA_KM2 — 返回给定分辨率下六边形的平均面积，单位为平方千米。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-km2.md
---

返回给定分辨率下六边形的平均面积，单位为平方千米。不包括五边形。

## Analyze 语法

```python
func.h3_area_km2(res)
```

## Analyze 示例

```python
func.h3_area_km2(1)

┌─────────────────────────┐
│ func.h3_hex_area_km2(1) │
├─────────────────────────┤
│       609788.4417941332 │
└─────────────────────────┘
```

## SQL 语法

```sql
H3_HEX_AREA_KM2(res)
```

## SQL 示例

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```
