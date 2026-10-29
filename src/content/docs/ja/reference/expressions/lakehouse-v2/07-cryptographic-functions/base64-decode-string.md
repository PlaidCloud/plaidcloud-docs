---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING — Base64 エンコードされた文字列を VARCHAR 文字列にデコードします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

Base64 エンコードされた文字列を VARCHAR 文字列にデコードします。

## Analyzeの構文

```python
func.base64_decode_string(<str>)
```

## Analyzeの例

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQLの構文

```sql
BASE64_DECODE_STRING(<str>)
```

## SQLの例

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
