---
title: H3_CELL_AREA_M2 (Lakehouse v1)
description: H3_CELL_AREA_M2 — gibt die exakte Fläche einer bestimmten Zelle in Quadratmetern zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-m2.md
---

Gibt die exakte Fläche einer bestimmten Zelle in Quadratmetern zurück.

## Analyze-Syntax

```python
func.h3_cell_area_m2(h3)
```

## Analyze-Beispiele

```python
func.h3_cell_area_m2(599119489002373119)

┌──────────────────────────────────────────┐
│ func.h3_cell_area_m2(599119489002373119) │
├──────────────────────────────────────────┤
│                       127785582.60809991 │
└──────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_CELL_AREA_M2(h3)
```

## SQL-Beispiele

```sql
SELECT H3_CELL_AREA_M2(599119489002373119);

┌─────────────────────────────────────┐
│ h3_cell_area_m2(599119489002373119) │
├─────────────────────────────────────┤
│                  127785582.60809991 │
└─────────────────────────────────────┘
```
