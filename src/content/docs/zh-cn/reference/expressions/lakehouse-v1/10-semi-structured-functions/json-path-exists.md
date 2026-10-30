---
title: JSON_PATH_EXISTS（Lakehouse v1）
description: JSON_PATH_EXISTS — 检查 JSON 数据中是否存在指定路径。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-exists.md
---

检查 JSON 数据中是否存在指定路径。

## Analyze 语法

```python
func.json_path_exists(<json_data>, <json_path_expression)
```

## Analyze 示例

```python
func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)'), func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)')
┌─────────────────────────────┐
│       Item 1   │  Item 2    │
├────────────────┼────────────┤
│       True     │  False     │
└─────────────────────────────┘
```

## SQL 语法

```sql
JSON_PATH_EXISTS(<json_data>, <json_path_expression>)
```

- json_data：指定要搜索的 JSON 数据。可以是 JSON 对象或数组。

- json_path_expression：指定要在 JSON 数据中检查的路径，路径从以 `$` 表示的 JSON 数据根节点开始。表达式中还可以包含条件，使用 `@` 引用当前正在计算的节点或元素，以筛选结果。

## 返回类型

该函数返回：

- 如果指定的 JSON 路径（及条件，如有）存在于 JSON 数据中，返回 `true`。
- 如果指定的 JSON 路径（及条件，如有）不存在于 JSON 数据中，返回 `false`。
- 如果 json_data 或 json_path_expression 为 NULL 或无效，返回 NULL。

## SQL 示例

```sql
SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)');

----
true


SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)');

----
false

SELECT JSON_PATH_EXISTS(NULL, '$.a');

----
NULL

SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), NULL);

----
NULL
```
