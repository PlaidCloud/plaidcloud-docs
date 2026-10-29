---
title: AES_DECRYPT (Lakehouse v2)
description: AES_DECRYPT — AES で暗号化された値を復号します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-decrypt.md
---

AES で暗号化された値を復号します。

## Analyzeの構文

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Analyzeの例

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## SQLの構文

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## SQLの例

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
