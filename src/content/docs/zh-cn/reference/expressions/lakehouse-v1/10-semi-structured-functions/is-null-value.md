---
title: IS_NULL_VALUE（Lakehouse v1）
description: IS_NULL_VALUE — 检查输入值是否为 JSON null。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-null-value.md
---

检查输入值是否为 JSON `null`。请注意，此函数检查的是 JSON `null`，而不是 SQL NULL。如需检查值是否为 SQL NULL，请使用 [IS_NULL](../../03-conditional-functions/is-null)。

```json title='JSON null Example:'
{
  "name": "John",
  "age": null
}   
```

## Analyze 语法

```python
func.is_null_value(<expr>)
```

## Analyze 示例

```python

func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5'))
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ true                                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
IS_NULL_VALUE( <expr> )
```

## 返回类型

如果输入值是 JSON `null`，则返回 `true`，否则返回 `false`。

## SQL 示例

```sql
SELECT
  IS_NULL_VALUE(PARSE_JSON('{"name":"John", "age":null}') :age), --JSON null
  IS_NULL(NULL); --SQL NULL

┌──────────────────────────────────────────────────────────────────────────────┐
│ is_null_value(parse_json('{"name":"john", "age":null}'):age) │ is_null(null) │
├──────────────────────────────────────────────────────────────┼───────────────┤
│ true                                                         │ true          │
└──────────────────────────────────────────────────────────────────────────────┘
```
