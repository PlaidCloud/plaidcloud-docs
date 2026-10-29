---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING — decodifica una cadena codificada en base64 y la convierte en una cadena VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

Decodifica una cadena codificada en base64 y la convierte en una cadena VARCHAR.

## Sintaxis de Analyze

```python
func.base64_decode_string(<str>)
```

## Ejemplos de Analyze

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
BASE64_DECODE_STRING(<str>)
```

## Ejemplos de SQL

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
