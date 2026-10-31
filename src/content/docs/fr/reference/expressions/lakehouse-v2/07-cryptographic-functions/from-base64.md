---
title: FROM_BASE64 (Lakehouse v2)
description: FROM_BASE64 — décode une chaîne encodée en base64. Alias de `BASE64_DECODE_STRING`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/from-base64.md
---

Décode une chaîne encodée en base64. Alias de `BASE64_DECODE_STRING`.

## Syntaxe Analyze

```python
func.from_base64(<str>)
```

## Exemples Analyze

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
FROM_BASE64(<str>)
```

## Exemples SQL

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
