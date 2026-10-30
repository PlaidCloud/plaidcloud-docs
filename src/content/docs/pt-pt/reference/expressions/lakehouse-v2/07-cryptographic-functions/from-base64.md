---
title: FROM_BASE64 (Lakehouse v2)
description: FROM_BASE64 — descodifica uma cadeia codificada em base64. Alias de `BASE64_DECODE_STRING`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/from-base64.md
---

Descodifica uma cadeia codificada em base64. Alias de `BASE64_DECODE_STRING`.

## Sintaxe do Analyze

```python
func.from_base64(<str>)
```

## Exemplos do Analyze

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
FROM_BASE64(<str>)
```

## Exemplos SQL

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
