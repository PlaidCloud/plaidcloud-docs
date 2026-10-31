---
title: "ELEMENT_AT (Map, Lakehouse v2)"
description: ELEMENT_AT – gibt den Wert zurück, der einem angegebenen Schlüssel in einer Map zugeordnet ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

Gibt den Wert zurück, der einem angegebenen Schlüssel in einer Map zugeordnet ist.

## Analyze-Syntax

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Analyze-Beispiele

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## SQL-Syntax

```sql
ELEMENT_AT(<map_col>, 'key')
```

## SQL-Beispiele

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
