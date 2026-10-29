---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING — decodifica uma string codificada em base64 em uma string VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

Decodifica uma string codificada em base64 em uma string VARCHAR.

## Sintaxe do Analyze

```python
func.base64_decode_string(<str>)
```

## Exemplos do Analyze

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
BASE64_DECODE_STRING(<str>)
```

## Exemplos SQL

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
