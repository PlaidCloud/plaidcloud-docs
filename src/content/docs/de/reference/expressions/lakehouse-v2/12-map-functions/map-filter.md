---
title: MAP_FILTER (Lakehouse v2)
description: MAP_FILTER – filtert Schlüssel-Wert-Paare in einer Map mithilfe eines Lambda-Ausdrucks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-filter.md
---

Filtert Schlüssel-Wert-Paare in einer Map mithilfe eines Lambda-Ausdrucks.

## Analyze-Syntax

```python
func.map_filter(get_column(table, 'map_col'), lambda k, v: v > 1)
```

## Analyze-Beispiele

```python
func.map_filter(MAP{'a':1,'b':2,'c':3}, lambda k,v: v>1)

┌───────────────┐
│ {'b':2,'c':3} │
└───────────────┘
```

## SQL-Syntax

```sql
MAP_FILTER(<map_col>, lambda k, v: v > 1)
```

## SQL-Beispiele

```sql
SELECT MAP_FILTER((k, v) -> v > 1, MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ {"b":2,"c":3} │
└───────────────┘
```
