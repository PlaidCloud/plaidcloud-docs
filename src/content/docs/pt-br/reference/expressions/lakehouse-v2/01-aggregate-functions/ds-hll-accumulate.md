---
title: DS_HLL_ACCUMULATE (Lakehouse v2)
description: "Use a função de agregação DS_HLL_ACCUMULATE no PlaidCloud Lakehouse. Acumula valores em um sketch HLL do DataSketches para contagem distinta aproximada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

Acumula valores em um sketch HLL do DataSketches para contagem distinta aproximada.

## Sintaxe no Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Exemplos no Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## Sintaxe SQL

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## Exemplos de SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
