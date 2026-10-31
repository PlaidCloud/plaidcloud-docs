---
title: BASE64_DECODE_BINARY (Lakehouse v2)
description: BASE64_DECODE_BINARY — dekoduje ciąg zakodowany w base64 do wartości binarnej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-binary.md
---

Dekoduje ciąg zakodowany w base64 do wartości binarnej.

## Składnia Analyze

```python
func.base64_decode_binary(<str>)
```

## Przykłady Analyze

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Składnia SQL

```sql
BASE64_DECODE_BINARY(<str>)
```

## Przykłady SQL

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
