---
title: "ELEMENT_AT (Mapa, Lakehouse v2)"
description: ELEMENT_AT — zwraca wartość powiązaną z podanym kluczem w mapie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

Zwraca wartość powiązaną z podanym kluczem w mapie.

## Składnia Analyze

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Przykłady Analyze

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## Składnia SQL

```sql
ELEMENT_AT(<map_col>, 'key')
```

## Przykłady SQL

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
