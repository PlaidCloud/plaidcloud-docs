---
title: H3_GET_BASE_CELL (Lakehouse v1)
description: H3_GET_BASE_CELL — devolve o número da célula de base do índice H3 indicado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-base-cell.md
---

Devolve o número da célula de base do índice [H3](https://eng.uber.com/h3/) indicado. 

## Sintaxe do Analyze

```python
func.h3_get_base_cell(h3)
```

## Exemplos do Analyze

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_GET_BASE_CELL(h3)
```

## Exemplos de SQL

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```
