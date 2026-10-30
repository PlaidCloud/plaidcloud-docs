---
title: AES_ENCRYPT (Lakehouse v2)
description: AES_ENCRYPT — chiffre une valeur avec le chiffrement AES.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-encrypt.md
---

Chiffre une valeur avec le chiffrement AES.

## Syntaxe Analyze

```python
func.aes_encrypt(<str>, <key>)
```

## Exemples Analyze

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## Syntaxe SQL

```sql
AES_ENCRYPT(<str>, <key>)
```

## Exemples SQL

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
