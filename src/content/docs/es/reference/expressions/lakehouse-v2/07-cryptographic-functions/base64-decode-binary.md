---
title: BASE64_DECODE_BINARY (Lakehouse v2)
description: BASE64_DECODE_BINARY — decodifica una cadena codificada en base64 y la convierte en un valor binario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-binary.md
---

Decodifica una cadena codificada en base64 y la convierte en un valor binario.

## Sintaxis de Analyze

```python
func.base64_decode_binary(<str>)
```

## Ejemplos de Analyze

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Sintaxis de SQL

```sql
BASE64_DECODE_BINARY(<str>)
```

## Ejemplos de SQL

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
