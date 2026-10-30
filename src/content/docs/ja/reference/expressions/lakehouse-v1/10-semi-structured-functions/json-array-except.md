---
title: JSON_ARRAY_EXCEPT (Lakehouse v1)
description: JSON_ARRAY_EXCEPT — 1つ目のJSON配列の要素のうち、2つ目のJSON配列に存在しない要素を含む新しいJSON配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-except.md
---

1つ目のJSON配列の要素のうち、2つ目のJSON配列に存在しない要素を含む新しいJSON配列を返します。

## SQL構文

```sql
JSON_ARRAY_EXCEPT(<json_array1>, <json_array2>)
```

## 戻り値の型

JSON配列。

## SQLの例

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
