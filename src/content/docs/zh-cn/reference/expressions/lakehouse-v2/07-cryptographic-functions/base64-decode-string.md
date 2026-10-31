---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING：将 base64 编码的字符串解码为 VARCHAR 字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

将 base64 编码的字符串解码为 VARCHAR 字符串。

## Analyze 语法

```python
func.base64_decode_string(<str>)
```

## Analyze 示例

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 语法

```sql
BASE64_DECODE_STRING(<str>)
```

## SQL 示例

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
