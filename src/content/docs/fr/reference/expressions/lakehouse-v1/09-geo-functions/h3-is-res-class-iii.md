---
title: H3_IS_RES_CLASS_III (Lakehouse v1)
description: H3_IS_RES_CLASS_III — vérifie si l'index H3 donné a une résolution d'orientation de classe III.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-res-class-iii.md
---

Vérifie si l'index [H3](https://eng.uber.com/h3/) donné a une résolution d'orientation de classe III.

## Syntaxe Analyze

```python
func.h3_is_res_class_iii(h3)
```

## Exemples Analyze

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_IS_RES_CLASS_III(h3)
```

## Exemples SQL

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```
