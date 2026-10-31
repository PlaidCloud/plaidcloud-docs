---
title: JSON_ARRAY_OVERLAP（Lakehouse v1）
description: JSON_ARRAY_OVERLAP — 检查两个 JSON 数组是否有重叠，存在共有元素时返回 true，否则返回 false。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

检查两个 JSON 数组是否有重叠，存在共有元素时返回 `true`，否则返回 `false`。

## SQL 语法

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## 返回类型

该函数返回布尔值：

- 两个 JSON 数组之间至少有一个共有元素时，返回 `true`，
- 没有共有元素时，返回 `false`。

## SQL 示例

```sql
SELECT json_array_overlap(
    '["apple", "banana", "cherry"]'::JSON,  
    '["banana", "kiwi", "mango"]'::JSON
);

-[ RECORD 1 ]-----------------------------------
json_array_overlap('["apple", "banana", "cherry"]'::VARIANT, '["banana", "kiwi", "mango"]'::VARIANT): true


SELECT json_array_overlap(
    '["grape", "orange"]'::JSON,  
    '["apple", "kiwi"]'::JSON     
);

-[ RECORD 1 ]-----------------------------------
json_array_overlap('["grape", "orange"]'::VARIANT, '["apple", "kiwi"]'::VARIANT): false
```
