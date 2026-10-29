---
title: BASE64_DECODE_BINARY (Lakehouse v2)
description: BASE64_DECODE_BINARY — décode une chaîne encodée en base64 en valeur binaire.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-binary.md
---

Décode une chaîne encodée en base64 en valeur binaire.

## Syntaxe Analyze

```python
func.base64_decode_binary(<str>)
```

## Exemples Analyze

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Syntaxe SQL

```sql
BASE64_DECODE_BINARY(<str>)
```

## Exemples SQL

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
