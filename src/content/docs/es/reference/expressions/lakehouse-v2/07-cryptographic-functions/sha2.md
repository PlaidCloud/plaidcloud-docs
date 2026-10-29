---
title: SHA2 (Lakehouse v2)
description: SHA2 — devuelve el hash SHA-2 de una cadena para una longitud de bits especificada (224, 256, 384 o 512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sha2.md
---

Devuelve el hash SHA-2 de una cadena para una longitud de bits especificada (224, 256, 384 o 512).

## Sintaxis de Analyze

```python
func.sha2(<str>, <bit_length>)
```

## Ejemplos de Analyze

```python
func.sha2('hello', 256)

┌───────────────┐
│ '2cf24dba...'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
SHA2(<str>, <bit_length>)
```

## Ejemplos de SQL

```sql
SELECT SHA2('hello', 256);

┌──────────────────────────────────────────────────────────────────┐
│ 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  │
└──────────────────────────────────────────────────────────────────┘
```
