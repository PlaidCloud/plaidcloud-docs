---
title: H3_IS_RES_CLASS_III (Lakehouse v1)
description: H3_IS_RES_CLASS_III — comprueba si el índice H3 dado tiene una resolución con orientación de Clase III.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-res-class-iii.md
---

Comprueba si el índice [H3](https://eng.uber.com/h3/) dado tiene una resolución con orientación de Clase III.

## Sintaxis de Analyze

```python
func.h3_is_res_class_iii(h3)
```

## Ejemplos de Analyze

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_IS_RES_CLASS_III(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```
