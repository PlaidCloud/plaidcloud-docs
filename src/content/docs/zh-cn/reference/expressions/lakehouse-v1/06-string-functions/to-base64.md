---
title: TO_BASE64（Lakehouse v1）
description: TO_BASE64——将字符串参数转换为 base-64 编码形式，并以字符串形式返回结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

将字符串参数转换为 base-64 编码形式，并以字符串形式返回结果。
如果参数不是字符串，则先转换为字符串再进行编码。
如果参数为 NULL，则结果为 NULL。

## Analyze 语法

```python
func.to_base64(<v>)
```

## Analyze 示例

```python
func.to_base64('abc')
┌───────────────────────┐
│ func.to_base64('abc') │
├───────────────────────┤
│ YWJj                  │
└───────────────────────┘
```

## SQL 语法

```sql
TO_BASE64(<v>)
```

## 参数

| 参数 | 说明 |
|-----------|-------------|
| `<v>`     | 值。  |

## 返回类型

`VARCHAR`

## SQL 示例

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
