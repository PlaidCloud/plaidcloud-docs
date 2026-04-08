---
title: AES_ENCRYPT
description: "Learn how to use the AES_ENCRYPT cryptographic function in PlaidCloud Lakehouse. Encrypts a value using AES encryption - see syntax, examples, and output."
---

Encrypts a value using AES encryption.

## Analyze Syntax

```python
func.aes_encrypt(<str>, <key>)
```

## Analyze Examples

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## SQL Syntax

```sql
AES_ENCRYPT(<str>, <key>)
```

## SQL Examples

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
