---
title: H3_TO_PARENT (Lakehouse v1)
description: H3_TO_PARENT — devuelve el índice padre que contiene h3 en la resolución parent_res.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-parent.md
---

Devuelve el índice padre que contiene `h3` en la resolución `parent_res`. Un resultado de 0 indica que se produjo un error.

## Sintaxis de Analyze

```python
func.h3_to_parent(h3, parent_res)
```

## Ejemplos de Analyze

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_TO_PARENT(h3, parent_res)
```

## Ejemplos de SQL

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```
