---
title: AES_ENCRYPT (Lakehouse v2)
description: AES_ENCRYPT — AES 暗号化を使用して値を暗号化します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-encrypt.md
---

AES 暗号化を使用して値を暗号化します。

## Analyzeの構文

```python
func.aes_encrypt(<str>, <key>)
```

## Analyzeの例

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## SQLの構文

```sql
AES_ENCRYPT(<str>, <key>)
```

## SQLの例

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
