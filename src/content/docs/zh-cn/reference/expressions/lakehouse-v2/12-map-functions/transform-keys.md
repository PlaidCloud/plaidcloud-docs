---
title: TRANSFORM_KEYS (Lakehouse v2)
description: TRANSFORM_KEYS — 应用 lambda 表达式转换映射的键。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-keys.md
---

应用 lambda 表达式转换映射的键。

## Analyze 语法

```python
func.transform_keys(get_column(table, 'map_col'), lambda k, v: upper(k))
```

## Analyze 示例

```python
func.transform_keys(MAP{'a':1,'b':2}, lambda k,v: upper(k))

┌───────────────┐
│ {'A':1,'B':2} │
└───────────────┘
```

## SQL 语法

```sql
TRANSFORM_KEYS(<map_col>, lambda k, v: upper(k))
```

## SQL 示例

```sql
SELECT TRANSFORM_KEYS((k, v) -> UPPER(k), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"A":1,"B":2} │
└───────────────┘
```
