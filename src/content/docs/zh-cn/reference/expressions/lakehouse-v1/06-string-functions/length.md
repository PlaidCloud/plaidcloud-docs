---
title: LENGTH（Lakehouse v1）
description: LENGTH——返回给定输入字符串或二进制值的长度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

返回给定输入字符串或二进制值的长度。对于字符串，长度表示字符数，每个 UTF-8 字符计为一个字符；对于二进制数据，长度对应字节数。

## Analyze 语法

```python
func.length(<expr>)
```

## Analyze 示例

```python
func.length('Hello')
┌──────────────────────┐
│ func.length('Hello') │
├──────────────────────┤
│                    5 │
└──────────────────────┘
```

## SQL 语法

```sql
LENGTH(<expr>)
```

## 别名

- [CHAR_LENGTH](../char-length)
- [CHARACTER_LENGTH](../character-length)
- [LENGTH_UTF8](../length-utf8)

## 返回类型

BIGINT

## SQL 示例

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
