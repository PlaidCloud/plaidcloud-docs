---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES — マップのすべての値を配列として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-values.md
---

マップのすべての値を配列として返します。

## Analyzeの構文

```python
func.map_values(get_column(table, 'map_col'))
```

## Analyzeの例

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## SQLの構文

```sql
MAP_VALUES(<map_col>)
```

## SQLの例

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
