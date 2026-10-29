---
title: MAP_SIZE（Lakehouse v1）
description: MAP_SIZE — 返回 MAP 的大小。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-size.md
---

返回 MAP 的大小。

## SQL 语法

```sql
MAP_SIZE( <map> )
```

## 参数

| 参数      | 说明         |
|-----------|--------------|
| `<map>`   | 输入 MAP。   |

## 返回类型

UInt64。

## SQL 示例

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
