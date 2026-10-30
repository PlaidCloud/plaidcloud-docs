---
title: AES_ENCRYPT (Lakehouse v2)
description: AES_ENCRYPT – verschlüsselt einen Wert mit AES-Verschlüsselung.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-encrypt.md
---

Verschlüsselt einen Wert mit AES-Verschlüsselung.

## Analyze-Syntax

```python
func.aes_encrypt(<str>, <key>)
```

## Analyze-Beispiele

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## SQL-Syntax

```sql
AES_ENCRYPT(<str>, <key>)
```

## SQL-Beispiele

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
