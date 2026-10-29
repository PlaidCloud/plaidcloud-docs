---
title: "CARDINALITY (Map, Lakehouse v2)"
description: CARDINALITY – gibt die Anzahl der Schlüssel-Wert-Paare in einer Map zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

Gibt die Anzahl der Schlüssel-Wert-Paare in einer Map zurück.

## Analyze-Syntax

```python
func.cardinality(get_column(table, 'map_col'))
```

## Analyze-Beispiele

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQL-Syntax

```sql
CARDINALITY(<map_col>)
```

## SQL-Beispiele

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
