---
title: H3_TO_GEO（Lakehouse v1）
description: H3_TO_GEO — 返回给定 H3 索引对应的经度和纬度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-geo.md
---

返回给定 [H3](https://eng.uber.com/h3/) 索引对应的经度和纬度。

## Analyze 语法

```python
func.h3_to_geo(h3)
```

## Analyze 示例

```python
func.h3_to_geo(644325524701193974)

┌────────────────────────────────────────┐
│   func.h3_to_geo(644325524701193974)   │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_TO_GEO(h3)
```

## SQL 示例

```sql
SELECT H3_TO_GEO(644325524701193974);

┌────────────────────────────────────────┐
│      h3_to_geo(644325524701193974)     │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```
