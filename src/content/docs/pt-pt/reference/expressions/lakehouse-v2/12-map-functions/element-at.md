---
title: "ELEMENT_AT (Mapa, Lakehouse v2)"
description: ELEMENT_AT — devolve o valor associado a uma chave especificada num mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

Devolve o valor associado a uma chave especificada num mapa.

## Sintaxe de Analyze

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Exemplos de Analyze

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## Sintaxe SQL

```sql
ELEMENT_AT(<map_col>, 'key')
```

## Exemplos SQL

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
