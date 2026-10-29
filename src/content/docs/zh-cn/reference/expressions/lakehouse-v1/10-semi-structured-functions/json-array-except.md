---
title: JSON_ARRAY_EXCEPT（Lakehouse v1）
description: JSON_ARRAY_EXCEPT — 返回一个新的 JSON 数组，包含第一个 JSON 数组中不存在于第二个 JSON 数组的元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-except.md
---

返回一个新的 JSON 数组，包含第一个 JSON 数组中不存在于第二个 JSON 数组的元素。

## SQL 语法

```sql
JSON_ARRAY_EXCEPT(<json_array1>, <json_array2>)
```

## 返回类型

JSON 数组。

## SQL 示例

```sql
SELECT JSON_ARRAY_EXCEPT(
    '["apple", "banana", "orange"]'::JSON,  
    '["banana", "grapes"]'::JSON         
);

-[ RECORD 1 ]-----------------------------------
json_array_except('["apple", "banana", "orange"]'::VARIANT, '["banana", "grapes"]'::VARIANT): ["apple","orange"]

-- Return an empty array because all elements in the first array are present in the second array.
SELECT json_array_except('["apple", "banana", "orange"]'::VARIANT, '["apple", "banana", "orange"]'::VARIANT)

-[ RECORD 1 ]-----------------------------------
json_array_except('["apple", "banana", "orange"]'::VARIANT, '["apple", "banana", "orange"]'::VARIANT): []
```
