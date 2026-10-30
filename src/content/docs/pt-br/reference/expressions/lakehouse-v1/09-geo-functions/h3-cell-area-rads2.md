---
title: H3_CELL_AREA_RADS2 (Lakehouse v1)
description: H3_CELL_AREA_RADS2 — retorna a área exata de uma célula específica em radianos quadrados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-rads2.md
---

Retorna a área exata de uma célula específica em radianos quadrados.

## Sintaxe do Analyze

```python
func.h3_cell_area_rads2(h3)
```

## Exemplos do Analyze

```python
func.h3_cell_area_rads2(599119489002373119)

┌─────────────────────────────────────────────┐
│ func.h3_cell_area_rads2(599119489002373119) │
├─────────────────────────────────────────────┤
│                     0.000003148224310427697 │
└─────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_CELL_AREA_RADS2(h3)
```

## Exemplos de SQL

```sql
SELECT H3_CELL_AREA_RADS2(599119489002373119);

┌────────────────────────────────────────┐
│ h3_cell_area_rads2(599119489002373119) │
├────────────────────────────────────────┤
│                0.000003148224310427697 │
└────────────────────────────────────────┘
```
