---
title: JSON_ARRAY_INSERT（Lakehouse v1）
description: JSON_ARRAY_INSERT — 在 JSON 数组的指定索引处插入值，并返回更新后的 JSON 数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-insert.md
---

在 JSON 数组的指定索引处插入值，并返回更新后的 JSON 数组。

## SQL 语法

```sql
JSON_ARRAY_INSERT(<json_array>, <index>, <json_value>)
```

| 参数           | 说明 |
|----------------|------|
| `<json_array>` | 要修改的 JSON 数组。 |
| `<index>`      | 插入值的位置。正索引在指定位置插入，超出范围时追加到末尾；负索引从末尾开始计位置插入，超出范围时插入到开头。 |
| `<json_value>` | 要插入数组的 JSON 值。 |

## 返回类型

JSON 数组。

## SQL 示例

当 `<index>` 为非负整数时，新元素插入到指定位置，现有元素向右移动。

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

负的 `<index>` 从数组末尾开始计数，`-1` 表示最后一个元素之前的位置，`-2` 表示倒数第二个元素之前，依此类推。

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
