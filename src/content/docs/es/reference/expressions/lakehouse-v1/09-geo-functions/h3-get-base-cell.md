---
title: H3_GET_BASE_CELL (Lakehouse v1)
description: H3_GET_BASE_CELL — devuelve el número de celda base del índice H3 dado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-base-cell.md
---

Devuelve el número de celda base del índice [H3](https://eng.uber.com/h3/) dado. 

## Sintaxis de Analyze

```python
func.h3_get_base_cell(h3)
```

## Ejemplos de Analyze

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_GET_BASE_CELL(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```
