---
title: FROM_BASE64 (Lakehouse v2)
description: FROM_BASE64 — dekoduje ciąg zakodowany w base64. Alias funkcji `BASE64_DECODE_STRING`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/from-base64.md
---

Dekoduje ciąg zakodowany w base64. Alias funkcji `BASE64_DECODE_STRING`.

## Składnia Analyze

```python
func.from_base64(<str>)
```

## Przykłady Analyze

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Składnia SQL

```sql
FROM_BASE64(<str>)
```

## Przykłady SQL

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
