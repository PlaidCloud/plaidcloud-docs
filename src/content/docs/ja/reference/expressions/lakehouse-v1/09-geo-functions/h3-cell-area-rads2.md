---
title: H3_CELL_AREA_RADS2（Lakehouse v1）
description: H3_CELL_AREA_RADS2 — 指定したセルの正確な面積を平方ラジアンで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-rads2.md
---

指定したセルの正確な面積を平方ラジアンで返します。

## Analyze Syntax

```python
func.h3_cell_area_rads2(h3)
```

## Analyze Examples

```python
func.h3_cell_area_rads2(599119489002373119)

┌─────────────────────────────────────────────┐
│ func.h3_cell_area_rads2(599119489002373119) │
├─────────────────────────────────────────────┤
│                     0.000003148224310427697 │
└─────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_CELL_AREA_RADS2(h3)
```

## SQL Examples

```sql
SELECT H3_CELL_AREA_RADS2(599119489002373119);

┌────────────────────────────────────────┐
│ h3_cell_area_rads2(599119489002373119) │
├────────────────────────────────────────┤
│                0.000003148224310427697 │
└────────────────────────────────────────┘
```
