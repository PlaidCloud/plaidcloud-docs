---
title: JSON_ARRAY_INSERT (Lakehouse v1)
description: JSON_ARRAY_INSERT — JSON配列の指定したインデックスの位置に値を挿入し、更新後のJSON配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-insert.md
---

JSON配列の指定したインデックスの位置に値を挿入し、更新後のJSON配列を返します。

## SQL構文

```sql
JSON_ARRAY_INSERT(<json_array>, <index>, <json_value>)
```

| パラメーター      | 説明                                                                                                                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<json_array>` | 変更するJSON配列です。                                                                                                                                                                                |
| `<index>`      | 値を挿入する位置です。正のインデックスは指定した位置に挿入し、範囲外の場合は末尾に追加します。負のインデックスは末尾から数えて挿入し、範囲外の場合は先頭に挿入します。 |
| `<json_value>` | 配列に挿入するJSON値です。                                                                                                                                                                 |

## 戻り値の型

JSON配列。

## SQLの例

`<index>` が0以上の整数の場合、新しい要素は指定した位置に挿入され、既存の要素は右にシフトされます。

```sql
-- The new element is inserted at position 0 (the beginning of the array), shifting all original elements to the right
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 0, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 0, '"new_task"'::VARIANT): ["new_task","task1","task2","task3"]

-- The new element is inserted at position 1, between task1 and task2
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 1, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 1, '"new_task"'::VARIANT): ["task1","new_task","task2","task3"]

-- If the index exceeds the length of the array, the new element is appended at the end of the array
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 6, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 6, '"new_task"'::VARIANT): ["task1","task2","task3","new_task"]
```

負の `<index>` は配列の末尾から数えます。`-1` は最後の要素の前、`-2` は最後から2番目の要素の前、というように指定します。

```sql
-- The new element is inserted just before the last element (task3)
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, -1, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, - 1, '"new_task"'::VARIANT): ["task1","task2","new_task","task3"]

-- Since the negative index exceeds the array’s length, the new element is inserted at the beginning
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, -6, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, - 6, '"new_task"'::VARIANT): ["new_task","task1","task2","task3"]
```
