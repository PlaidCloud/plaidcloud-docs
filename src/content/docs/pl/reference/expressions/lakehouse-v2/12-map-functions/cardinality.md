---
title: "CARDINALITY (Mapa, Lakehouse v2)"
description: CARDINALITY — zwraca liczbę par klucz-wartość w mapie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

Zwraca liczbę par klucz-wartość w mapie.

## Składnia Analyze

```python
func.cardinality(get_column(table, 'map_col'))
```

## Przykłady Analyze

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## Składnia SQL

```sql
CARDINALITY(<map_col>)
```

## Przykłady SQL

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
