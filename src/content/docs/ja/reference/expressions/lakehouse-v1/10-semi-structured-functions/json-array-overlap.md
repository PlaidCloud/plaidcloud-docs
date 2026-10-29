---
title: JSON_ARRAY_OVERLAP (Lakehouse v1)
description: JSON_ARRAY_OVERLAP — 2つのJSON配列に重複があるかどうかをチェックし、共通する要素がある場合は true、ない場合は false を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

2つのJSON配列に重複があるかどうかをチェックし、共通する要素がある場合は `true`、ない場合は `false` を返します。

## SQL構文

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## 戻り値の型

この関数はブール値を返します。

- 2つのJSON配列に共通する要素が1つ以上ある場合は `true`
- 共通する要素がない場合は `false`

## SQLの例

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
