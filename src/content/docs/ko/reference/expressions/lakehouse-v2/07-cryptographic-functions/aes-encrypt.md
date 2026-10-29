---
title: AES_ENCRYPT (Lakehouse v2)
description: AES_ENCRYPT — AES 암호화를 사용하여 값을 암호화합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-encrypt.md
---

AES 암호화를 사용하여 값을 암호화합니다.

## Analyze 구문

```python
func.aes_encrypt(<str>, <key>)
```

## Analyze 예제

```python
func.aes_encrypt('hello', 'secret_key')

┌──────────┐
│ (binary)  │
└──────────┘
```

## SQL 구문

```sql
AES_ENCRYPT(<str>, <key>)
```

## SQL 예제

```sql
SELECT HEX(AES_ENCRYPT('hello', 'secret_key'));

┌──────────┐
│ A7B4C...  │
└──────────┘
```
