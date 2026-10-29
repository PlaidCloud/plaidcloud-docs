---
title: JSON_ARRAY_INSERT (Lakehouse v1)
description: JSON_ARRAY_INSERT — JSON 배열의 지정한 인덱스에 값을 삽입하고 업데이트된 JSON 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-insert.md
---

JSON 배열의 지정한 인덱스에 값을 삽입하고 업데이트된 JSON 배열을 반환합니다.

## SQL Syntax

```sql
JSON_ARRAY_INSERT(<json_array>, <index>, <json_value>)
```

| 매개변수      | 설명                                                                                                                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<json_array>` | 수정할 JSON 배열입니다.                                                                                                                                                                                |
| `<index>`      | 값을 삽입할 위치입니다. 양수 인덱스는 지정한 위치에 삽입하며, 범위를 벗어나면 끝에 추가합니다. 음수 인덱스는 끝에서부터 계산해 삽입하며, 범위를 벗어나면 맨 앞에 삽입합니다. |
| `<json_value>` | 배열에 삽입할 JSON 값입니다.                                                                                                                                                                 |

## 반환 타입

JSON 배열.

## SQL Examples

`<index>`가 음수가 아닌 정수이면 새 요소가 지정한 위치에 삽입되고 기존 요소는 오른쪽으로 밀립니다.

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

음수 `<index>`는 배열의 끝에서부터 계산하며, `-1`은 마지막 요소 앞 위치, `-2`는 끝에서 두 번째 요소 앞 위치를 뜻합니다.

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
