---
title: JSON_ARRAY_DISTINCT（Lakehouse v1）
description: JSON_ARRAY_DISTINCT — 从 JSON 数组中删除重复元素，并返回仅包含不重复元素的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-distinct.md
---

从 JSON 数组中删除重复元素，并返回仅包含不重复元素的数组。

## SQL 语法

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## 返回类型

JSON 数组。

## SQL 示例

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
