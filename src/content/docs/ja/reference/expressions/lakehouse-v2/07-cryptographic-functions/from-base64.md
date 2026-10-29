---
title: FROM_BASE64 (Lakehouse v2)
description: FROM_BASE64 — Base64 エンコードされた文字列をデコードします。`BASE64_DECODE_STRING` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/from-base64.md
---

Base64 エンコードされた文字列をデコードします。`BASE64_DECODE_STRING` の別名です。

## Analyzeの構文

```python
func.from_base64(<str>)
```

## Analyzeの例

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQLの構文

```sql
FROM_BASE64(<str>)
```

## SQLの例

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
