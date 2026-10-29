---
title: DS_HLL_ACCUMULATE (Lakehouse v2)
description: "Użyj funkcji agregującej DS_HLL_ACCUMULATE w PlaidCloud Lakehouse. Gromadzi wartości w szkicu HLL DataSketches do przybliżonego zliczania unikatowych wartości."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

Gromadzi wartości w szkicu HLL DataSketches do przybliżonego zliczania unikatowych wartości.

## Składnia Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Przykłady Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## Składnia SQL

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## Przykłady SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
