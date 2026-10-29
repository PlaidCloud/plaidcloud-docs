---
title: H3_TO_GEO（Lakehouse v1）
description: H3_TO_GEO — 指定したH3インデックスに対応する経度と緯度を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-geo.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスに対応する経度と緯度を返します。

## Analyze Syntax

```python
func.h3_to_geo(h3)
```

## Analyze Examples

```python
func.h3_to_geo(644325524701193974)

┌────────────────────────────────────────┐
│   func.h3_to_geo(644325524701193974)   │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_TO_GEO(h3)
```

## SQL Examples

```sql
SELECT H3_TO_GEO(644325524701193974);

┌────────────────────────────────────────┐
│      h3_to_geo(644325524701193974)     │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```
