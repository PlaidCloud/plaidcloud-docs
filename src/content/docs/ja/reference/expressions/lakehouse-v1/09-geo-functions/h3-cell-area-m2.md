---
title: H3_CELL_AREA_M2（Lakehouse v1）
description: H3_CELL_AREA_M2 — 指定したセルの正確な面積を平方メートルで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-m2.md
---

指定したセルの正確な面積を平方メートルで返します。

## Analyze Syntax

```python
func.h3_cell_area_m2(h3)
```

## Analyze Examples

```python
func.h3_cell_area_m2(599119489002373119)

┌──────────────────────────────────────────┐
│ func.h3_cell_area_m2(599119489002373119) │
├──────────────────────────────────────────┤
│                       127785582.60809991 │
└──────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_CELL_AREA_M2(h3)
```

## SQL Examples

```sql
SELECT H3_CELL_AREA_M2(599119489002373119);

┌─────────────────────────────────────┐
│ h3_cell_area_m2(599119489002373119) │
├─────────────────────────────────────┤
│                  127785582.60809991 │
└─────────────────────────────────────┘
```
