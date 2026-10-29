---
title: "ELEMENT_AT (Map, Lakehouse v2)"
description: ELEMENT_AT — renvoie la valeur associée à une clé spécifiée dans un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

Renvoie la valeur associée à une clé spécifiée dans un map.

## Syntaxe Analyze

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Exemples Analyze

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## Syntaxe SQL

```sql
ELEMENT_AT(<map_col>, 'key')
```

## Exemples SQL

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
