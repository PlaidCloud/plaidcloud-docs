---
title: BASE64_DECODE_BINARY (Lakehouse v2)
description: BASE64_DECODE_BINARY：将 base64 编码的字符串解码为二进制值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-binary.md
---

将 base64 编码的字符串解码为二进制值。

## Analyze 语法

```python
func.base64_decode_binary(<str>)
```

## Analyze 示例

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL 语法

```sql
BASE64_DECODE_BINARY(<str>)
```

## SQL 示例

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
