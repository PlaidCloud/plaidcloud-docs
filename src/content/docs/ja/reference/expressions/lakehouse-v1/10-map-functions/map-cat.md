---
title: MAP_CAT（Lakehouse v1）
description: MAP_CAT — 2つのMAPを連結した結果を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

2つのMAPを連結した結果を返します。

## SQL Syntax

```sql
MAP_CAT( <map1>, <map2> )
```

## 引数

| 引数 | 説明                     |
|-----------|---------------------------------|
| `<map1>`  | 元のMAP。                 |
| `<map2>`  | map1に追加するMAP。 |

:::note
- map1とmap2に同じキーを持つ値がある場合、出力のマップにはmap2の値が含まれます。
- いずれかの引数がNULLの場合、この関数はエラーを報告せずにNULLを返します。
:::

## 戻り値の型

Map。

## SQL Examples

```sql
SELECT MAP_CAT({'a':1,'b':2,'c':3}, {'c':5,'d':6});
┌─────────────────────────────────────────────┐
│ map_cat({'a':1,'b':2,'c':3}, {'c':5,'d':6}) │
├─────────────────────────────────────────────┤
│ {'a':1,'b':2,'c':5,'d':6}                   │
└─────────────────────────────────────────────┘
```
