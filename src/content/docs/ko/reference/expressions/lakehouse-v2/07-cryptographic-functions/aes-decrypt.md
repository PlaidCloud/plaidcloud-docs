---
title: AES_DECRYPT (Lakehouse v2)
description: AES_DECRYPT — AES로 암호화된 값을 복호화합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/aes-decrypt.md
---

AES로 암호화된 값을 복호화합니다.

## Analyze 구문

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Analyze 예제

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## SQL 구문

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## SQL 예제

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
