---
title: H3_GET_BASE_CELL (Lakehouse v1)
description: H3_GET_BASE_CELL — zwraca numer komórki bazowej podanego indeksu H3.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-base-cell.md
---

Zwraca numer komórki bazowej podanego indeksu [H3](https://eng.uber.com/h3/). 

## Składnia Analyze

```python
func.h3_get_base_cell(h3)
```

## Przykłady Analyze

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_GET_BASE_CELL(h3)
```

## Przykłady SQL

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```
