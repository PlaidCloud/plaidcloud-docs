---
title: H3_NUM_HEXAGONS (Lakehouse v1)
description: H3_NUM_HEXAGONS — renvoie le nombre d'index H3 uniques à la résolution donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-num-hexagons.md
---

Renvoie le nombre d'index [H3](https://eng.uber.com/h3/) uniques à la résolution donnée.

## Syntaxe Analyze

```python
func.h3_num_hexagons(res)
```

## Exemples Analyze

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## Syntaxe SQL

```sql
H3_NUM_HEXAGONS(res)
```

## Exemples SQL

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```
