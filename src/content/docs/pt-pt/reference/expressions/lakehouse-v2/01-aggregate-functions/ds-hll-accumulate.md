---
title: DS_HLL_ACCUMULATE (Lakehouse v2)
description: "Utilize a função de agregação DS_HLL_ACCUMULATE no PlaidCloud Lakehouse. Acumula valores num sketch HLL do DataSketches para contagem distinta aproximada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

Acumula valores num sketch HLL do DataSketches para contagem distinta aproximada.

## Sintaxe do Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Exemplos do Analyze

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
