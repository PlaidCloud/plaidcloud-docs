---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES — zwraca wszystkie wartości z mapy jako tablicę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-values.md
---

Zwraca wszystkie wartości z mapy jako tablicę.

## Składnia Analyze

```python
func.map_values(get_column(table, 'map_col'))
```

## Przykłady Analyze

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## Składnia SQL

```sql
MAP_VALUES(<map_col>)
```

## Przykłady SQL

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
