---
title: MAP_CAT（Lakehouse v1）
description: MAP_CAT — 返回两个 MAP 的拼接结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

返回两个 MAP 的拼接结果。

## SQL 语法

```sql
MAP_CAT( <map1>, <map2> )
```

## 参数

| 参数      | 说明                           |
|-----------|--------------------------------|
| `<map1>`  | 源 MAP。                       |
| `<map2>`  | 要追加到 map1 的 MAP。         |

:::note
- 如果 map1 和 map2 中有相同键的值，则输出的 MAP 包含 map2 中的值。
- 如果任一参数为 NULL，函数返回 NULL，且不报告任何错误。
:::

## 返回类型

Map。

## SQL 示例

```sql
SELECT MAP_CAT({'a':1,'b':2,'c':3}, {'c':5,'d':6});
┌─────────────────────────────────────────────┐
│ map_cat({'a':1,'b':2,'c':3}, {'c':5,'d':6}) │
├─────────────────────────────────────────────┤
│ {'a':1,'b':2,'c':5,'d':6}                   │
└─────────────────────────────────────────────┘
```
