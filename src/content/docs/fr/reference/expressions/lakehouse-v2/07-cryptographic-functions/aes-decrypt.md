---
title: AES_DECRYPT (Lakehouse v2)
description: AES_DECRYPT — déchiffre une valeur chiffrée avec AES.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-decrypt.md
---

Déchiffre une valeur chiffrée avec AES.

## Syntaxe Analyze

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Exemples Analyze

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## Syntaxe SQL

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## Exemples SQL

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
