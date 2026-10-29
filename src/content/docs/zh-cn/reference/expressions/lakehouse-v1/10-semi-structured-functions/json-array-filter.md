---
title: JSON_ARRAY_FILTER（Lakehouse v1）
description: JSON_ARRAY_FILTER — 根据指定的 Lambda 筛选 JSON 数组中的元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

根据指定的 Lambda 表达式筛选 JSON 数组中的元素，仅返回满足条件的元素。有关 Lambda 表达式的更多信息，请参阅 Lambda 表达式。

## SQL 语法

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## 返回类型

JSON 数组。

## SQL 示例

此示例筛选数组，仅返回以字母 `a` 开头的字符串，结果为 `["apple", "avocado"]`：

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
