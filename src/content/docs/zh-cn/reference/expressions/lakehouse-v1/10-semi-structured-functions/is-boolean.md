---
title: IS_BOOLEAN（Lakehouse v1）
description: IS_BOOLEAN — 检查输入的 JSON 值是否为布尔值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-boolean.md
---

检查输入的 JSON 值是否为布尔值。

## Analyze 语法

```python
func.is_boolean(<expr>)
```

## Analyze 示例

```python

func.is_boolean(func.parse_json('true')), func.is_boolean(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_boolean(func.parse_json('true')) │ func.is_boolean(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
IS_BOOLEAN( <expr> )
```

## 返回类型

如果输入的 JSON 值是布尔值，则返回 `true`，否则返回 `false`。

## SQL 示例

```sql
SELECT
  IS_BOOLEAN(PARSE_JSON('true')),
  IS_BOOLEAN(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────────┐
│ is_boolean(parse_json('true')) │ is_boolean(parse_json('[1,2,3]')) │
├────────────────────────────────┼───────────────────────────────────┤
│ true                           │ false                             │
└────────────────────────────────────────────────────────────────────┘
```
