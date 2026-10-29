---
title: H3_GET_BASE_CELL (Lakehouse v1)
description: H3_GET_BASE_CELL — renvoie le numéro de la cellule de base de l'index H3 donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-base-cell.md
---

Renvoie le numéro de la cellule de base de l'index [H3](https://eng.uber.com/h3/) donné.

## Syntaxe Analyze

```python
func.h3_get_base_cell(h3)
```

## Exemples Analyze

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_GET_BASE_CELL(h3)
```

## Exemples SQL

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```
