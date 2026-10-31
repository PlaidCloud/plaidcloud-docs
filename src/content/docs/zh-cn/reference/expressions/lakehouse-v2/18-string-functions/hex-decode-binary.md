---
title: HEX_DECODE_BINARY (Lakehouse v2)
description: HEX_DECODE_BINARY：将十六进制字符串解码为二进制值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-binary.md
---

将十六进制字符串解码为二进制值。

## Analyze 语法

```python
func.hex_decode_binary(<hex_str>)
```

## Analyze 示例

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL 语法

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## SQL 示例

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
