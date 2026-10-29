---
title: MAP_PICK（Lakehouse v1）
description: MAP_PICK — 既存のMAPから指定したキーと値のペアを含む新しいMAPを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-pick.md
---

既存のMAPから指定したキーと値のペアを含む新しいMAPを返します。

## SQL Syntax

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## 引数

| 引数 | 説明                                             |
|-----------|-------------------------------------------------------- |
| `<map>`   | 入力MAP。                                          |
| `<keyN>`  | 返されるMAPに含めるKEY。          |
| `<array>` | 返されるMAPに含めるKEYの配列。 |

:::note
- キー式の型と、マップ内のキーの型は同じである必要があります。
- マップ内に見つからないキーの値は無視されます。
:::

## 戻り値の型

Map。

## SQL Examples

```sql
SELECT MAP_PICK({'a':1,'b':2,'c':3}, 'a', 'c');
┌─────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, 'a', 'c') │
├─────────────────────────────────────────┤
│ {'a':1,'c':3}                           │
└─────────────────────────────────────────┘

SELECT MAP_PICK({'a':1,'b':2,'c':3}, ['a', 'b']);
┌───────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, ['a', 'b']) │
├───────────────────────────────────────────┤
│ {'a':1,'b':2}                             │
└───────────────────────────────────────────┘
```
