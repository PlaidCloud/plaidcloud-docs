---
title: MAP_VALUES（Lakehouse v1）
description: MAP_VALUES — 返回 MAP 中的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-values.md
---

返回 MAP 中的值。

## SQL 语法

```sql
MAP_VALUES( <map> )
```

## 参数

| 参数      | 说明         |
|-----------|--------------|
| `<map>`   | 输入 MAP。   |

## 返回类型

Array。

## SQL 示例

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
