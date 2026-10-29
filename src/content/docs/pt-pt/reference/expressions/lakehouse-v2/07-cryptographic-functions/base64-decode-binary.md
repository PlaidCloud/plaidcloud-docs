---
title: BASE64_DECODE_BINARY (Lakehouse v2)
description: BASE64_DECODE_BINARY — descodifica uma cadeia codificada em base64 para um valor binário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-binary.md
---

Descodifica uma cadeia codificada em base64 para um valor binário.

## Sintaxe do Analyze

```python
func.base64_decode_binary(<str>)
```

## Exemplos do Analyze

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Sintaxe SQL

```sql
BASE64_DECODE_BINARY(<str>)
```

## Exemplos SQL

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
