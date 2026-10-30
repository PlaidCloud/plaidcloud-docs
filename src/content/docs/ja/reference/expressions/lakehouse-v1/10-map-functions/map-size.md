---
title: MAP_SIZE（Lakehouse v1）
description: MAP_SIZE — MAPのサイズを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-size.md
---

MAPのサイズを返します。

## SQL Syntax

```sql
MAP_SIZE( <map> )
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<map>`   | 入力マップ。 |

## 戻り値の型

UInt64。

## SQL Examples

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
