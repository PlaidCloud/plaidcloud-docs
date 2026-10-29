---
title: DS_HLL_COUNT_DISTINCT (Lakehouse v2)
description: "Verwenden Sie die Aggregatfunktion DS_HLL_COUNT_DISTINCT in PlaidCloud Lakehouse. Sie gibt mit dem DataSketches-HLL-Algorithmus eine ungefähre Anzahl eindeutiger Werte zurück. Genauer als APPROX_COUNT_DISTINCT."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-count-distinct.md
---

Gibt mit dem DataSketches-HLL-Algorithmus eine ungefähre Anzahl eindeutiger Werte zurück. Genauer als `APPROX_COUNT_DISTINCT`.

## Analyze-Syntax

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))
```

## Analyze-Beispiele

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10042 │
└───────┘
```

## SQL-Syntax

```sql
DS_HLL_COUNT_DISTINCT(<expr>)
```

## SQL-Beispiele

```sql
SELECT DS_HLL_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10042 │
└───────┘
```
