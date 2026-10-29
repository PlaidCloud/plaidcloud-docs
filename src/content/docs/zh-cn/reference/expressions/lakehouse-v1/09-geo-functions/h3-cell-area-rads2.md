---
title: H3_CELL_AREA_RADS2（Lakehouse v1）
description: H3_CELL_AREA_RADS2 — 返回指定单元的精确面积，单位为平方弧度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-rads2.md
---

返回指定单元的精确面积，单位为平方弧度。

## Analyze 语法

```python
func.h3_cell_area_rads2(h3)
```

## Analyze 示例

```python
func.h3_cell_area_rads2(599119489002373119)

┌─────────────────────────────────────────────┐
│ func.h3_cell_area_rads2(599119489002373119) │
├─────────────────────────────────────────────┤
│                     0.000003148224310427697 │
└─────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_CELL_AREA_RADS2(h3)
```

## SQL 示例

```sql
SELECT H3_CELL_AREA_RADS2(599119489002373119);

┌────────────────────────────────────────┐
│ h3_cell_area_rads2(599119489002373119) │
├────────────────────────────────────────┤
│                0.000003148224310427697 │
└────────────────────────────────────────┘
```
