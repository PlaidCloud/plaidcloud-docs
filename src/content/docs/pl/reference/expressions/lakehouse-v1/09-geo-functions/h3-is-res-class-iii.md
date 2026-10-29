---
title: H3_IS_RES_CLASS_III (Lakehouse v1)
description: H3_IS_RES_CLASS_III — sprawdza, czy podany indeks H3 ma rozdzielczość o orientacji klasy III.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-res-class-iii.md
---

Sprawdza, czy podany indeks [H3](https://eng.uber.com/h3/) ma rozdzielczość o orientacji klasy III.

## Składnia Analyze

```python
func.h3_is_res_class_iii(h3)
```

## Przykłady Analyze

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_IS_RES_CLASS_III(h3)
```

## Przykłady SQL

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```
