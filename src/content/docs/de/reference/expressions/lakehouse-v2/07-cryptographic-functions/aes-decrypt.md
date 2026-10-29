---
title: AES_DECRYPT (Lakehouse v2)
description: AES_DECRYPT – entschlüsselt einen mit AES verschlüsselten Wert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-decrypt.md
---

Entschlüsselt einen mit AES verschlüsselten Wert.

## Analyze-Syntax

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Analyze-Beispiele

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## SQL-Syntax

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## SQL-Beispiele

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
