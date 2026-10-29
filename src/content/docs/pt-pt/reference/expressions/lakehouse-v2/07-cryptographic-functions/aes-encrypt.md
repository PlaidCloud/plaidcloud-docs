---
title: AES_ENCRYPT (Lakehouse v2)
description: AES_ENCRYPT — encripta um valor através de encriptação AES.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-encrypt.md
---

Encripta um valor através de encriptação AES.

## Sintaxe do Analyze

```python
func.aes_encrypt(<str>, <key>)
```

## Exemplos do Analyze

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## Sintaxe SQL

```sql
AES_ENCRYPT(<str>, <key>)
```

## Exemplos SQL

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
