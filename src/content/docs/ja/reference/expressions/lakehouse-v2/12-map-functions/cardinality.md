---
title: "CARDINALITY (Map, Lakehouse v2)"
description: CARDINALITY — マップ内のキーと値のペアの数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

マップ内のキーと値のペアの数を返します。

## Analyzeの構文

```python
func.cardinality(get_column(table, 'map_col'))
```

## Analyzeの例

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQLの構文

```sql
CARDINALITY(<map_col>)
```

## SQLの例

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
