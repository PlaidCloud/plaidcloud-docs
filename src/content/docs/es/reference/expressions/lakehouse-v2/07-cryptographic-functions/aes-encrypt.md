---
title: AES_ENCRYPT (Lakehouse v2)
description: AES_ENCRYPT — cifra un valor mediante cifrado AES.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-encrypt.md
---

Cifra un valor mediante cifrado AES.

## Sintaxis de Analyze

```python
func.aes_encrypt(<str>, <key>)
```

## Ejemplos de Analyze

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## Sintaxis de SQL

```sql
AES_ENCRYPT(<str>, <key>)
```

## Ejemplos de SQL

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
