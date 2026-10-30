---
title: MAP_INSERT（Lakehouse v1）
description: MAP_INSERT — 入力MAPに新しいキーと値のペアを挿入した（既存のキーは新しい値で更新した）新しいMAPを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-insert.md
---

入力MAPに新しいキーと値のペアを挿入した（既存のキーは新しい値で更新した）新しいMAPを返します。

## SQL Syntax

```sql
MAP_INSERT( <map>, <key>, <value> [, <updateFlag> ] )
```

## 引数

| 引数      | 説明                                                                                  |
|----------------|----------------------------------------------------------------------------------------------|
| `<map>`        | 入力MAP。                                                                               |
| `<key>`        | MAPに挿入する新しいキー。                                                          |
| `<value>`      | MAPに挿入する新しい値。                                                        |
| `<updateFlag>` | 既存のキーを上書きできるかどうかを示すブール値のフラグ。デフォルトはFALSEです。 |

## 戻り値の型

Map。

## SQL Examples

```sql
SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'd', 4);
┌─────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'd', 4) │
├─────────────────────────────────────────┤
│ {'a':1,'b':2,'c':3,'d':4}               │
└─────────────────────────────────────────┘

SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'a', 5, true);
┌───────────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'a', 5, TRUE) │
├───────────────────────────────────────────────┤
│ {'a':5,'b':2,'c':3}                           │
└───────────────────────────────────────────────┘
```
