---
title: BASE64_DECODE_BINARY (Lakehouse v2)
description: BASE64_DECODE_BINARY – dekodiert eine Base64-kodierte Zeichenfolge in einen Binärwert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-binary.md
---

Dekodiert eine Base64-kodierte Zeichenfolge in einen Binärwert.

## Analyze-Syntax

```python
func.base64_decode_binary(<str>)
```

## Analyze-Beispiele

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL-Syntax

```sql
BASE64_DECODE_BINARY(<str>)
```

## SQL-Beispiele

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
