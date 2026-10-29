---
title: JSON_ARRAY_REDUCE（Lakehouse v1）
description: JSON_ARRAY_REDUCE — 通过应用指定的 Lambda 表达式，将 JSON 数组归约为单个值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-reduce.md
---

通过应用指定的 Lambda 表达式，将 JSON 数组归约为单个值。有关 Lambda 表达式的更多信息，请参阅 Lambda 表达式。

## SQL 语法

```sql
JSON_ARRAY_REDUCE(<json_array>, <lambda_expression>)
```

## SQL 示例

此示例将数组中的所有元素相乘（2 _ 3 _ 4）：

```sql
SELECT JSON_ARRAY_REDUCE(
    [2, 3, 4]::JSON,
    (acc, d) -> acc::Int * d::Int
);

-[ RECORD 1 ]-----------------------------------
json_array_reduce([2, 3, 4]::VARIANT, (acc, d) -> acc::Int32 * d::Int32): 24
```
