---
title: MAP_VALUES（Lakehouse v1）
description: MAP_VALUES — マップ内の値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-values.md
---

マップ内の値を返します。

## SQL Syntax

```sql
MAP_VALUES( <map> )
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<map>`   | 入力マップ。 |

## 戻り値の型

Array。

## SQL Examples

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
