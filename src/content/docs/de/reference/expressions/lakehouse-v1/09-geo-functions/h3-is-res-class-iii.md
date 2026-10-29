---
title: H3_IS_RES_CLASS_III (Lakehouse v1)
description: H3_IS_RES_CLASS_III — prüft, ob der angegebene H3-Index eine Auflösung mit Class-III-Ausrichtung hat.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-res-class-iii.md
---

Prüft, ob der angegebene [H3](https://eng.uber.com/h3/)-Index eine Auflösung mit Class-III-Ausrichtung hat.

## Analyze-Syntax

```python
func.h3_is_res_class_iii(h3)
```

## Analyze-Beispiele

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_IS_RES_CLASS_III(h3)
```

## SQL-Beispiele

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```
