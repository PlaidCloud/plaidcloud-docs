---
title: FROM_BASE64 (Lakehouse v2)
description: FROM_BASE64 – dekodiert eine Base64-kodierte Zeichenfolge. Alias für `BASE64_DECODE_STRING`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/from-base64.md
---

Dekodiert eine Base64-kodierte Zeichenfolge. Alias für `BASE64_DECODE_STRING`.

## Analyze-Syntax

```python
func.from_base64(<str>)
```

## Analyze-Beispiele

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL-Syntax

```sql
FROM_BASE64(<str>)
```

## SQL-Beispiele

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
