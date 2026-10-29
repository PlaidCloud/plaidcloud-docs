---
title: TRANSFORM_KEYS (Lakehouse v2)
description: TRANSFORM_KEYS — ラムダ式を適用して、マップのキーを変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-keys.md
---

ラムダ式を適用して、マップのキーを変換します。

## Analyzeの構文

```python
func.transform_keys(get_column(table, 'map_col'), lambda k, v: upper(k))
```

## Analyzeの例

```python
func.transform_keys(MAP{'a':1,'b':2}, lambda k,v: upper(k))

┌───────────────┐
│ {'A':1,'B':2} │
└───────────────┘
```

## SQLの構文

```sql
TRANSFORM_KEYS(<map_col>, lambda k, v: upper(k))
```

## SQLの例

```sql
SELECT TRANSFORM_KEYS((k, v) -> UPPER(k), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"A":1,"B":2} │
└───────────────┘
```
