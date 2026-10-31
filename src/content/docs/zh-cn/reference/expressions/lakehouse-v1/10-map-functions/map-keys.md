---
title: MAP_KEYS（Lakehouse v1）
description: MAP_KEYS — 返回 MAP 中的键。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-keys.md
---

返回 MAP 中的键。

## SQL 语法

```sql
MAP_KEYS( <map> )
```

## 参数

| 参数      | 说明         |
|-----------|--------------|
| `<map>`   | 输入 MAP。   |

## 返回类型

Array。

## SQL 示例

```sql
SELECT MAP_KEYS({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_keys({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ ['a','b','c']                 │
└───────────────────────────────┘
```
