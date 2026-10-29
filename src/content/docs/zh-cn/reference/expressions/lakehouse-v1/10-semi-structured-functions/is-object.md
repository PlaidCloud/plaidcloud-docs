---
title: IS_OBJECT（Lakehouse v1）
description: IS_OBJECT — 检查输入值是否为 JSON 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-object.md
---

检查输入值是否为 JSON 对象。

## Analyze 语法

```python
func.is_object(<expr>)
```

## Analyze 示例

```python

func.is_object(func.parse_json('{"a":"b"}')), func.is_object(func.parse_json('["a","b","c"]'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_object(func.parse_json('{"a":"b"}'))  │ func.is_object(func.parse_json('["a","b","c"]')) │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
IS_OBJECT( <expr> )
```

## 返回类型

如果输入的 JSON 值是 JSON 对象，则返回 `true`，否则返回 `false`。

## SQL 示例

```sql
SELECT
  IS_OBJECT(PARSE_JSON('{"a":"b"}')), -- JSON Object
  IS_OBJECT(PARSE_JSON('["a","b","c"]')); --JSON Array

┌─────────────────────────────────────────────────────────────────────────────┐
│ is_object(parse_json('{"a":"b"}')) │ is_object(parse_json('["a","b","c"]')) │
├────────────────────────────────────┼────────────────────────────────────────┤
│ true                               │ false                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```
