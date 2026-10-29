---
title: IS_ARRAY（Lakehouse v1）
description: IS_ARRAY — 检查输入值是否为 JSON 数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-array.md
---

检查输入值是否为 JSON 数组。请注意，JSON 数组与 ARRAY 数据类型不同。JSON 数组是 JSON 中常用的数据结构，表示由方括号 `[ ]` 括起来的有序值集合。它是一种灵活的格式，可用于组织和交换各种数据类型，包括字符串、数字、布尔值、对象和 null。

```json title='JSON Array Example:'
[
  "Apple",
  42,
  true,
  {"name": "John", "age": 30, "isStudent": false},
  [1, 2, 3],
  null
]
```

## Analyze 语法

```python
func.is_array(<expr>)
```

## Analyze 示例

```python

func.is_array(func.parse_json('true')), func.is_array(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_array(func.parse_json('true')) │ func.is_array(func.parse_json('[1,2,3]')) │
├────────────────────────────────────────┼───────────────────────────────────────────┤
│ false                                  │ true                                      │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
IS_ARRAY( <expr> )
```

## 返回类型

如果输入值是 JSON 数组，则返回 `true`，否则返回 `false`。

## SQL 示例

```sql
SELECT
  IS_ARRAY(PARSE_JSON('true')),
  IS_ARRAY(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────┐
│ is_array(parse_json('true')) │ is_array(parse_json('[1,2,3]')) │
├──────────────────────────────┼─────────────────────────────────┤
│ false                        │ true                            │
└────────────────────────────────────────────────────────────────┘
```
