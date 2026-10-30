---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING — décode une chaîne encodée en base64 en chaîne VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

Décode une chaîne encodée en base64 en chaîne VARCHAR.

## Syntaxe Analyze

```python
func.base64_decode_string(<str>)
```

## Exemples Analyze

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
BASE64_DECODE_STRING(<str>)
```

## Exemples SQL

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
