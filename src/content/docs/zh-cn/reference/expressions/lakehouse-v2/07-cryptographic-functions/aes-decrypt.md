---
title: AES_DECRYPT (Lakehouse v2)
description: AES_DECRYPT：解密使用 AES 加密的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-decrypt.md
---

解密使用 AES 加密的值。

## Analyze 语法

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Analyze 示例

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## SQL 语法

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## SQL 示例

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
