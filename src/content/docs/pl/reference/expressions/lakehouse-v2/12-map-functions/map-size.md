---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE — zwraca liczbę par klucz-wartość w mapie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

Zwraca liczbę par klucz-wartość w mapie.

## Składnia Analyze

```python
func.map_size(get_column(table, 'map_col'))
```

## Przykłady Analyze

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## Składnia SQL

```sql
MAP_SIZE(<map_col>)
```

## Przykłady SQL

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
