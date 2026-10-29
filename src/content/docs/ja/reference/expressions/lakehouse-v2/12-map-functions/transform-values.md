---
title: TRANSFORM_VALUES (Lakehouse v2)
description: TRANSFORM_VALUES — ラムダ式を適用して、マップの値を変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-values.md
---

ラムダ式を適用して、マップの値を変換します。

## Analyzeの構文

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Analyzeの例

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQLの構文

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## SQLの例

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
