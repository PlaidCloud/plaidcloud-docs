---
title: BASE64_DECODE_BINARY (Lakehouse v2)
description: BASE64_DECODE_BINARY — Base64 エンコードされた文字列をバイナリ値にデコードします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-binary.md
---

Base64 エンコードされた文字列をバイナリ値にデコードします。

## Analyzeの構文

```python
func.base64_decode_binary(<str>)
```

## Analyzeの例

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQLの構文

```sql
BASE64_DECODE_BINARY(<str>)
```

## SQLの例

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
