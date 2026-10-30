---
title: AES_DECRYPT (Lakehouse v2)
description: AES_DECRYPT — descifra un valor cifrado con AES.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-decrypt.md
---

Descifra un valor cifrado con AES.

## Sintaxis de Analyze

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Ejemplos de Analyze

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## Ejemplos de SQL

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
