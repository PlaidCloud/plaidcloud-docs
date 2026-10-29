---
title: H3_CELL_AREA_RADS2 (Lakehouse v1)
description: H3_CELL_AREA_RADS2 — gibt die exakte Fläche einer bestimmten Zelle in Quadratradiant zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-rads2.md
---

Gibt die exakte Fläche einer bestimmten Zelle in Quadratradiant zurück.

## Analyze-Syntax

```python
func.h3_cell_area_rads2(h3)
```

## Analyze-Beispiele

```python
func.h3_cell_area_rads2(599119489002373119)

┌─────────────────────────────────────────────┐
│ func.h3_cell_area_rads2(599119489002373119) │
├─────────────────────────────────────────────┤
│                     0.000003148224310427697 │
└─────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_CELL_AREA_RADS2(h3)
```

## SQL-Beispiele

```sql
SELECT H3_CELL_AREA_RADS2(599119489002373119);

┌────────────────────────────────────────┐
│ h3_cell_area_rads2(599119489002373119) │
├────────────────────────────────────────┤
│                0.000003148224310427697 │
└────────────────────────────────────────┘
```
