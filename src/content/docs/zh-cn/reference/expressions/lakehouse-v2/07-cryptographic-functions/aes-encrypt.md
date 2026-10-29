---
title: AES_ENCRYPT (Lakehouse v2)
description: AES_ENCRYPT：使用 AES 加密算法加密值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-encrypt.md
---

使用 AES 加密算法加密值。

## Analyze 语法

```python
func.aes_encrypt(<str>, <key>)
```

## Analyze 示例

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## SQL 语法

```sql
AES_ENCRYPT(<str>, <key>)
```

## SQL 示例

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
