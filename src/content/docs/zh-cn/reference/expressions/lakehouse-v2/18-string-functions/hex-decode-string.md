---
title: HEX_DECODE_STRING (Lakehouse v2)
description: HEX_DECODE_STRING：将十六进制字符串解码为 VARCHAR 字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-string.md
---

将十六进制字符串解码为 VARCHAR 字符串。

## Analyze 语法

```python
func.hex_decode_string(<hex_str>)
```

## Analyze 示例

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 语法

```sql
HEX_DECODE_STRING(<hex_str>)
```

## SQL 示例

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
