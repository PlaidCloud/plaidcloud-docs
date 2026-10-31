---
title: JSON_ARRAY_DISTINCT (Lakehouse v1)
description: JSON_ARRAY_DISTINCT — JSON配列から重複する要素を削除し、一意な要素だけを含む配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-distinct.md
---

JSON配列から重複する要素を削除し、一意な要素だけを含む配列を返します。

## SQL構文

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## 戻り値の型

JSON配列。

## SQLの例

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
