---
title: AES_ENCRYPT (Lakehouse v2)
description: AES_ENCRYPT — szyfruje wartość algorytmem AES.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-encrypt.md
---

Szyfruje wartość algorytmem AES.

## Składnia Analyze

```python
func.aes_encrypt(<str>, <key>)
```

## Przykłady Analyze

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## Składnia SQL

```sql
AES_ENCRYPT(<str>, <key>)
```

## Przykłady SQL

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
