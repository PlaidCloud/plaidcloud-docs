---
title: TO_BASE64 (Lakehouse v2)
description: TO_BASE64 — 文字列を Base64 エンコードされた文字列にエンコードします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/to-base64.md
---

文字列を Base64 エンコードされた文字列にエンコードします。

## Analyzeの構文

```python
func.to_base64(<str>)
```

## Analyzeの例

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## SQLの構文

```sql
TO_BASE64(<str>)
```

## SQLの例

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
