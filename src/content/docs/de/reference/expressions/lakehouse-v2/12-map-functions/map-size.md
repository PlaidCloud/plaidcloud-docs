---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE – gibt die Anzahl der Schlüssel-Wert-Paare in einer Map zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

Gibt die Anzahl der Schlüssel-Wert-Paare in einer Map zurück.

## Analyze-Syntax

```python
func.map_size(get_column(table, 'map_col'))
```

## Analyze-Beispiele

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQL-Syntax

```sql
MAP_SIZE(<map_col>)
```

## SQL-Beispiele

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
