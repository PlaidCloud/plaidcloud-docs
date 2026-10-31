---
title: FROM_BASE64 (Lakehouse v2)
description: FROM_BASE64 — decodifica una cadena codificada en base64. Alias de `BASE64_DECODE_STRING`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/from-base64.md
---

Decodifica una cadena codificada en base64. Alias de `BASE64_DECODE_STRING`.

## Sintaxis de Analyze

```python
func.from_base64(<str>)
```

## Ejemplos de Analyze

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
FROM_BASE64(<str>)
```

## Ejemplos de SQL

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
