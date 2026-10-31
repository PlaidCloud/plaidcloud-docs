---
title: PARSE_JSON（Lakehouse v1）
description: 将输入的 JSON 字符串解释为 JSON，生成 VARIANT 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/parse-json.md
---

`parse_json` 和 `try_parse_json` 将输入字符串解释为 JSON 文档，生成 VARIANT 值。

`try_parse_json` 在解析过程中发生错误时返回 NULL 值。

## Analyze 语法

```python
func.parse_json(<json_string>)

or

func.try_parse_json(<json_string>)
```

## Analyze 示例

```python
func.parse_json('[-1, 12, 289, 2188, false]')

┌───────────────────────────────────────────────┐
│ func.parse_json('[-1, 12, 289, 2188, false]') │
├───────────────────────────────────────────────┤
│ [-1,12,289,2188,false]                        │
└───────────────────────────────────────────────┘

func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ')

┌──────────────────────────────────────────────────────────────┐
│ func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├──────────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                                 │
└──────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
PARSE_JSON(<expr>)
TRY_PARSE_JSON(<expr>)
```

## 参数

| 参数     | 说明 |
|----------|------|
| `<expr>` | 字符串类型（例如 VARCHAR）的表达式，包含有效的 JSON 信息。 |

## 返回类型

VARIANT

## SQL 示例

```sql
SELECT parse_json('[-1, 12, 289, 2188, false]');
┌──────────────────────────────────────────┐
│ parse_json('[-1, 12, 289, 2188, false]') │
├──────────────────────────────────────────┤
│ [-1,12,289,2188,false]                   │
└──────────────────────────────────────────┘

SELECT try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ');
┌─────────────────────────────────────────────────────────┐
│ try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├─────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                            │
└─────────────────────────────────────────────────────────┘
```
