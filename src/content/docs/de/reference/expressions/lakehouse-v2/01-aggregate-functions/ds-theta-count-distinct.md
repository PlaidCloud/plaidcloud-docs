---
title: DS_THETA_COUNT_DISTINCT (Lakehouse v2)
description: "Verwenden Sie die Aggregatfunktion DS_THETA_COUNT_DISTINCT in PlaidCloud Lakehouse. Sie gibt mit dem DataSketches-Theta-Algorithmus eine ungefähre Anzahl eindeutiger Werte zurück und unterstützt Mengenoperationen."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-theta-count-distinct.md
---

Gibt mit dem DataSketches-Theta-Algorithmus eine ungefähre Anzahl eindeutiger Werte zurück. Unterstützt Mengenoperationen wie Schnittmenge und Differenz.

## Analyze-Syntax

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Analyze-Beispiele

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10035 │
└───────┘
```

## SQL-Syntax

```sql
DS_THETA_COUNT_DISTINCT(<expr>)
```

## SQL-Beispiele

```sql
SELECT DS_THETA_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10035 │
└───────┘
```
