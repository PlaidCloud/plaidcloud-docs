---
title: MAP_INSERT（Lakehouse v1）
description: MAP_INSERT — 返回一个新 MAP，由插入了新键值对（或用新值更新现有键）的输入 MAP 构成。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-insert.md
---

返回一个新 MAP，由插入了新键值对（或用新值更新现有键）的输入 MAP 构成。

## SQL 语法

```sql
MAP_INSERT( <map>, <key>, <value> [, <updateFlag> ] )
```

## 参数

| 参数           | 说明                                                   |
|----------------|--------------------------------------------------------|
| `<map>`        | 输入 MAP。                                             |
| `<key>`        | 要插入 MAP 的新键。                                    |
| `<value>`      | 要插入 MAP 的新值。                                    |
| `<updateFlag>` | 布尔标志，指示是否可以覆盖现有键。默认为 FALSE。       |

## 返回类型

Map。

## SQL 示例

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
