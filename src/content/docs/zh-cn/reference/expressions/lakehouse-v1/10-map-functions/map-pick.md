---
title: MAP_PICK（Lakehouse v1）
description: MAP_PICK — 返回一个新 MAP，包含现有 MAP 中指定的键值对。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-pick.md
---

返回一个新 MAP，包含现有 MAP 中指定的键值对。

## SQL 语法

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## 参数

| 参数      | 说明                                  |
|-----------|---------------------------------------|
| `<map>`   | 输入 MAP。                            |
| `<keyN>`  | 要包含在返回的 MAP 中的键。           |
| `<array>` | 要包含在返回的 MAP 中的键的数组。     |

:::note
- 键表达式的类型必须与 MAP 中键的类型相同。
- 在 MAP 中找不到的键值会被忽略。
:::

## 返回类型

Map。

## SQL 示例

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
