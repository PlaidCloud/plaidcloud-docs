---
title: DS_HLL_ACCUMULATE (Lakehouse v2)
description: "Utilisez la fonction d'agrégation DS_HLL_ACCUMULATE dans PlaidCloud Lakehouse. Accumule des valeurs dans un sketch HLL DataSketches pour un comptage distinct approximatif."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

Accumule des valeurs dans un sketch HLL DataSketches pour un comptage distinct approximatif.

## Syntaxe Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Exemples Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## Syntaxe SQL

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## Exemples SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
