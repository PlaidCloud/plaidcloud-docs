---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING — dekoduje ciąg zakodowany w base64 do ciągu VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

Dekoduje ciąg zakodowany w base64 do ciągu VARCHAR.

## Składnia Analyze

```python
func.base64_decode_string(<str>)
```

## Przykłady Analyze

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Składnia SQL

```sql
BASE64_DECODE_STRING(<str>)
```

## Przykłady SQL

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
