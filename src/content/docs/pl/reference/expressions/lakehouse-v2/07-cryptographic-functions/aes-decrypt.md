---
title: AES_DECRYPT (Lakehouse v2)
description: AES_DECRYPT — odszyfrowuje wartość zaszyfrowaną algorytmem AES.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-decrypt.md
---

Odszyfrowuje wartość zaszyfrowaną algorytmem AES.

## Składnia Analyze

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Przykłady Analyze

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## Składnia SQL

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## Przykłady SQL

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
