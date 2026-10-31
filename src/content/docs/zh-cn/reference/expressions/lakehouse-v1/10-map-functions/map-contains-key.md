---
title: MAP_CONTAINS_KEY（Lakehouse v1）
description: MAP_CONTAINS_KEY — 判断指定 MAP 是否包含指定的键。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-contains-key.md
---

判断指定 MAP 是否包含指定的键。

## SQL 语法

```sql
MAP_CONTAINS_KEY( <map>, <key> )
```

## 参数

| 参数      | 说明               |
|-----------|--------------------|
| `<map>`   | 要搜索的 MAP。     |
| `<key>`   | 要查找的键。       |

## 返回类型

Boolean。

## SQL 示例

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
