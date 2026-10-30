---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING – dekodiert eine Base64-kodierte Zeichenfolge in eine VARCHAR-Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

Dekodiert eine Base64-kodierte Zeichenfolge in eine VARCHAR-Zeichenfolge.

## Analyze-Syntax

```python
func.base64_decode_string(<str>)
```

## Analyze-Beispiele

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL-Syntax

```sql
BASE64_DECODE_STRING(<str>)
```

## SQL-Beispiele

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
