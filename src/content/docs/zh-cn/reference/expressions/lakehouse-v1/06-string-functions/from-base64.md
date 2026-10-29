---
title: FROM_BASE64（Lakehouse v1）
description: FROM_BASE64——接收按 base-64 编码规则编码的字符串，并以二进制形式返回解码结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/from-base64.md
---

接收按 base-64 编码规则编码的字符串，并以二进制形式返回解码结果。
如果参数为 NULL 或不是有效的 base-64 字符串，则结果为 NULL。

## Analyze 语法

```python
func.from_base64(<expr>)
```

## Analyze 示例

```python
func.from_base64('YWJj')
┌──────────────────────────┐
│ func.from_base64('YWJj') │
├──────────────────────────┤
│ abc                      │
└──────────────────────────┘
```

## SQL 语法

```sql
FROM_BASE64(<expr>)
```

## 参数

| 参数 | 说明       |
|-----------|-------------------|
| `<expr>`  | 字符串值。 |

## 返回类型

`BINARY`

## SQL 示例

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
