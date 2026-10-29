---
title: H3_GET_BASE_CELL (Lakehouse v1)
description: H3_GET_BASE_CELL — gibt die Basiszellennummer des angegebenen H3-Index zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-base-cell.md
---

Gibt die Basiszellennummer des angegebenen [H3](https://eng.uber.com/h3/)-Index zurück.

## Analyze-Syntax

```python
func.h3_get_base_cell(h3)
```

## Analyze-Beispiele

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_GET_BASE_CELL(h3)
```

## SQL-Beispiele

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```
