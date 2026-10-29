---
title: "ELEMENT_AT (Map, Lakehouse v2)"
description: ELEMENT_AT — マップ内で指定したキーに対応する値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

マップ内で指定したキーに対応する値を返します。

## Analyzeの構文

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Analyzeの例

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## SQLの構文

```sql
ELEMENT_AT(<map_col>, 'key')
```

## SQLの例

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
