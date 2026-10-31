---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING — descodifica uma cadeia codificada em base64 para uma cadeia VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

Descodifica uma cadeia codificada em base64 para uma cadeia VARCHAR.

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
