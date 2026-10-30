---
title: MAP_KEYS（Lakehouse v1）
description: MAP_KEYS — マップ内のキーを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-keys.md
---

マップ内のキーを返します。

## SQL Syntax

```sql
MAP_KEYS( <map> )
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<map>`   | 入力マップ。 |

## 戻り値の型

Array。

## SQL Examples

```sql
SELECT MAP_KEYS({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_keys({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ ['a','b','c']                 │
└───────────────────────────────┘
```
