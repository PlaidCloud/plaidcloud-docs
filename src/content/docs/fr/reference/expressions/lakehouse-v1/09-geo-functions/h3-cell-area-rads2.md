---
title: H3_CELL_AREA_RADS2 (Lakehouse v1)
description: H3_CELL_AREA_RADS2 — renvoie la superficie exacte d'une cellule donnée, en radians carrés.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-rads2.md
---

Renvoie la superficie exacte d'une cellule donnée, en radians carrés.

## Syntaxe Analyze

```python
func.h3_cell_area_rads2(h3)
```

## Exemples Analyze

```python
func.h3_cell_area_rads2(599119489002373119)

┌─────────────────────────────────────────────┐
│ func.h3_cell_area_rads2(599119489002373119) │
├─────────────────────────────────────────────┤
│                     0.000003148224310427697 │
└─────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_CELL_AREA_RADS2(h3)
```

## Exemples SQL

```sql
SELECT H3_CELL_AREA_RADS2(599119489002373119);

┌────────────────────────────────────────┐
│ h3_cell_area_rads2(599119489002373119) │
├────────────────────────────────────────┤
│                0.000003148224310427697 │
└────────────────────────────────────────┘
```
