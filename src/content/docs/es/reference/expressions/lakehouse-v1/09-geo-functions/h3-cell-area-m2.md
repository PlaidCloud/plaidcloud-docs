---
title: H3_CELL_AREA_M2 (Lakehouse v1)
description: H3_CELL_AREA_M2 — devuelve el área exacta de una celda específica en metros cuadrados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-m2.md
---

Devuelve el área exacta de una celda específica en metros cuadrados.

## Sintaxis de Analyze

```python
func.h3_cell_area_m2(h3)
```

## Ejemplos de Analyze

```python
func.h3_cell_area_m2(599119489002373119)

┌──────────────────────────────────────────┐
│ func.h3_cell_area_m2(599119489002373119) │
├──────────────────────────────────────────┤
│                       127785582.60809991 │
└──────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_CELL_AREA_M2(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_CELL_AREA_M2(599119489002373119);

┌─────────────────────────────────────┐
│ h3_cell_area_m2(599119489002373119) │
├─────────────────────────────────────┤
│                  127785582.60809991 │
└─────────────────────────────────────┘
```
