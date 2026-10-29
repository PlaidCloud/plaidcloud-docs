---
title: MAP_DELETE（Lakehouse v1）
description: MAP_DELETE — 1つ以上のキーを削除した既存のMAPを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-delete.md
---

1つ以上のキーを削除した既存のMAPを返します。

## SQL Syntax

```sql
MAP_DELETE( <map>, <key1> [, <key2>, ... ] )
MAP_DELETE( <map>, <array> )
```

## 引数

| 引数 | 説明                                            |
|-----------|--------------------------------------------------------|
| `<map>`   | 削除するKEYを含むMAP。               |
| `<keyN>`  | 返されるMAPから除外するKEY。          |
| `<array>` | 返されるMAPから除外するKEYの配列。 |

:::note
- キー式の型と、マップ内のキーの型は同じである必要があります。
- マップ内に見つからないキーの値は無視されます。
:::

## 戻り値の型

Map。

## SQL Examples

```sql
SELECT MAP_DELETE({'a':1,'b':2,'c':3}, 'a', 'c');
┌───────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, 'a', 'c') │
├───────────────────────────────────────────┤
│ {'b':2}                                   │
└───────────────────────────────────────────┘

SELECT MAP_DELETE({'a':1,'b':2,'c':3}, ['a', 'b']);
┌─────────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, ['a', 'b']) │
├─────────────────────────────────────────────┤
│ {'c':3}                                     │
└─────────────────────────────────────────────┘
```
