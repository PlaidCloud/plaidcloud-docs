---
title: MAP_CONTAINS_KEY（Lakehouse v1）
description: MAP_CONTAINS_KEY — 指定したMAPに、指定したキーが含まれているかどうかを判定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-contains-key.md
---

指定したMAPに、指定したキーが含まれているかどうかを判定します。

## SQL Syntax

```sql
MAP_CONTAINS_KEY( <map>, <key> )
```

## 引数

| 引数 | 説明             |
|-----------|-------------------------|
| `<map>`   | 検索対象のマップ。 |
| `<key>`   | 検索するキー。        |

## 戻り値の型

Boolean。

## SQL Examples

```sql
SELECT MAP_CONTAINS_KEY({'a':1,'b':2,'c':3}, 'c');
┌────────────────────────────────────────────┐
│ map_contains_key({'a':1,'b':2,'c':3}, 'c') │
├────────────────────────────────────────────┤
│ true                                       │
└────────────────────────────────────────────┘

SELECT MAP_CONTAINS_KEY({'a':1,'b':2,'c':3}, 'x');
┌────────────────────────────────────────────┐
│ map_contains_key({'a':1,'b':2,'c':3}, 'x') │
├────────────────────────────────────────────┤
│ false                                      │
└────────────────────────────────────────────┘
```
