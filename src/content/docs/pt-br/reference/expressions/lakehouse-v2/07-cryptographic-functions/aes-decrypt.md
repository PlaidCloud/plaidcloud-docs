---
title: AES_DECRYPT (Lakehouse v2)
description: AES_DECRYPT — descriptografa um valor criptografado com AES.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-decrypt.md
---

Descriptografa um valor criptografado com AES.

## Sintaxe do Analyze

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Exemplos do Analyze

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## Sintaxe SQL

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## Exemplos SQL

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
