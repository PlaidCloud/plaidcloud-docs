---
title: H3_IS_RES_CLASS_III (Lakehouse v1)
description: H3_IS_RES_CLASS_III — verifica se o índice H3 indicado tem uma resolução com orientação de Classe III.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-res-class-iii.md
---

Verifica se o índice [H3](https://eng.uber.com/h3/) indicado tem uma resolução com orientação de Classe III.

## Sintaxe do Analyze

```python
func.h3_is_res_class_iii(h3)
```

## Exemplos do Analyze

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_IS_RES_CLASS_III(h3)
```

## Exemplos de SQL

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```
