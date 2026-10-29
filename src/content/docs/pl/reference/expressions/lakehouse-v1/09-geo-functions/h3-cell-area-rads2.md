---
title: H3_CELL_AREA_RADS2 (Lakehouse v1)
description: H3_CELL_AREA_RADS2 — zwraca dokładną powierzchnię danej komórki w radianach kwadratowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-rads2.md
---

Zwraca dokładną powierzchnię danej komórki w radianach kwadratowych.

## Składnia Analyze

```python
func.h3_cell_area_rads2(h3)
```

## Przykłady Analyze

```python
func.h3_cell_area_rads2(599119489002373119)

┌─────────────────────────────────────────────┐
│ func.h3_cell_area_rads2(599119489002373119) │
├─────────────────────────────────────────────┤
│                     0.000003148224310427697 │
└─────────────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_CELL_AREA_RADS2(h3)
```

## Przykłady SQL

```sql
SELECT H3_CELL_AREA_RADS2(599119489002373119);

┌────────────────────────────────────────┐
│ h3_cell_area_rads2(599119489002373119) │
├────────────────────────────────────────┤
│                0.000003148224310427697 │
└────────────────────────────────────────┘
```
