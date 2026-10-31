---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES – gibt alle Werte einer Map als Array zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-values.md
---

Gibt alle Werte einer Map als Array zurück.

## Analyze-Syntax

```python
func.map_values(get_column(table, 'map_col'))
```

## Analyze-Beispiele

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## SQL-Syntax

```sql
MAP_VALUES(<map_col>)
```

## SQL-Beispiele

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
