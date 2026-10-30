---
title: H3_TO_PARENT (Lakehouse v1)
description: H3_TO_PARENT — retorna o índice pai que contém h3 na resolução parent_res.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-parent.md
---

Retorna o índice pai que contém `h3` na resolução `parent_res`. Um retorno igual a 0 significa que ocorreu um erro.

## Sintaxe do Analyze

```python
func.h3_to_parent(h3, parent_res)
```

## Exemplos do Analyze

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_TO_PARENT(h3, parent_res)
```

## Exemplos de SQL

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```
