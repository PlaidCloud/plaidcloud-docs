---
title: AES_DECRYPT
description: "Learn how to use the AES_DECRYPT cryptographic function in PlaidCloud Lakehouse. Decrypts a value encrypted with AES - see syntax, examples, and output."
---

Decrypts a value encrypted with AES.

## Analyze Syntax

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Analyze Examples

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## SQL Syntax

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## SQL Examples

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
