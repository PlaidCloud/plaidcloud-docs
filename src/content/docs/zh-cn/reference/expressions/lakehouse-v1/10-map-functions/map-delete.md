---
title: MAP_DELETE（Lakehouse v1）
description: MAP_DELETE — 返回删除了一个或多个键的现有 MAP。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-delete.md
---

返回删除了一个或多个键的现有 MAP。

## SQL 语法

```sql
MAP_DELETE( <map>, <key1> [, <key2>, ... ] )
MAP_DELETE( <map>, <array> )
```

## 参数

| 参数      | 说明                                 |
|-----------|--------------------------------------|
| `<map>`   | 包含要删除的键的 MAP。               |
| `<keyN>`  | 要从返回的 MAP 中省略的键。          |
| `<array>` | 要从返回的 MAP 中省略的键的数组。    |

:::note
- 键表达式的类型必须与 MAP 中键的类型相同。
- 在 MAP 中找不到的键值会被忽略。
:::

## 返回类型

Map。

## SQL 示例

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
