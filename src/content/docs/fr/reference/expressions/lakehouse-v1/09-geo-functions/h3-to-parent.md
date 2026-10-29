---
title: H3_TO_PARENT (Lakehouse v1)
description: H3_TO_PARENT — renvoie l'index parent contenant h3 à la résolution parent_res.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-parent.md
---

Renvoie l'index parent contenant `h3` à la résolution `parent_res`. Une valeur renvoyée de 0 signale qu'une erreur s'est produite.

## Syntaxe Analyze

```python
func.h3_to_parent(h3, parent_res)
```

## Exemples Analyze

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_TO_PARENT(h3, parent_res)
```

## Exemples SQL

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```
