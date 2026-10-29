---
title: DS_HLL_ACCUMULATE (Lakehouse v2)
description: "Verwenden Sie die Aggregatfunktion DS_HLL_ACCUMULATE in PlaidCloud Lakehouse. Sie akkumuliert Werte in einem DataSketches-HLL-Sketch für die ungefähre Zählung eindeutiger Werte."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

Akkumuliert Werte in einem DataSketches-HLL-Sketch für die ungefähre Zählung eindeutiger Werte.

## Analyze-Syntax

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Analyze-Beispiele

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## SQL-Syntax

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## SQL-Beispiele

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
