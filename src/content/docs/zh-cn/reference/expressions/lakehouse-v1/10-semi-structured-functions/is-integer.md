---
title: IS_INTEGER（Lakehouse v1）
description: IS_INTEGER — 检查输入的 JSON 值是否为整数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-integer.md
---

检查输入的 JSON 值是否为整数。

## Analyze 语法

```python
func.is_integer(<expr>)
```

## Analyze 示例

```python

func.is_integer(func.parse_json('123')), func.is_integer(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_integer(func.parse_json('123'))  │ func.is_integer(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
IS_INTEGER( <expr> )
```

## 返回类型

如果输入的 JSON 值是整数，则返回 `true`，否则返回 `false`。

## SQL 示例

```sql
SELECT
  IS_INTEGER(PARSE_JSON('123')),
  IS_INTEGER(PARSE_JSON('[1,2,3]'));

┌───────────────────────────────────────────────────────────────────┐
│ is_integer(parse_json('123')) │ is_integer(parse_json('[1,2,3]')) │
├───────────────────────────────┼───────────────────────────────────┤
│ true                          │ false                             │
└───────────────────────────────────────────────────────────────────┘
```
