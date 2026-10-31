---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE — マップ内のキーと値のペアの数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

マップ内のキーと値のペアの数を返します。

## Analyzeの構文

```python
func.map_size(get_column(table, 'map_col'))
```

## Analyzeの例

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQLの構文

```sql
MAP_SIZE(<map_col>)
```

## SQLの例

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
