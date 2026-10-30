---
title: "ELEMENT_AT (Mapa, Lakehouse v2)"
description: ELEMENT_AT — retorna o valor associado a uma chave especificada em um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

Retorna o valor associado a uma chave especificada em um mapa.

## Sintaxe do Analyze

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
