---
title: CHECK_JSON（Lakehouse v1）
description: CHECK_JSON — 检查 JSON 文档是否有效。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/check-json.md
---

检查 JSON 文档是否有效。
如果输入字符串是有效的 JSON 文档或 `NULL`，则输出为 `NULL`。
如果输入无法转换为有效的 JSON 值，则输出字符串包含错误消息。

## Analyze 语法

```python
func.check_json(<expr>)
```

## Analyze 示例

```python
func.check_json('[1,2,3]');
┌────────────────────────────┐
│ func.check_json('[1,2,3]') │
├────────────────────────────┤
│ NULL                       │
└────────────────────────────┘
```

## SQL 语法

```sql
CHECK_JSON( <expr> )
```

## 参数

| 参数     | 说明             |
|----------|------------------|
| `<expr>` | 字符串类型的表达式 |

## 返回类型

String

## SQL 示例

```sql
SELECT check_json('[1,2,3]');
┌───────────────────────┐
│ check_json('[1,2,3]') │
├───────────────────────┤
│ NULL                  │
└───────────────────────┘

SELECT check_json('{"key":"val"}');
┌─────────────────────────────┐
│ check_json('{"key":"val"}') │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘

SELECT check_json('{"key":');
┌──────────────────────────────────────────────┐
│ check_json('{"key":')                        │
├──────────────────────────────────────────────┤
│ EOF while parsing a value at line 1 column 7 │
└──────────────────────────────────────────────┘
```
