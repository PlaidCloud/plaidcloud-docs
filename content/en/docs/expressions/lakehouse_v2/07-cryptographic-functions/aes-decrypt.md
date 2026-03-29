---
title: AES_DECRYPT
---

Decrypts a value encrypted with AES.

## Analyze Syntax

```python
func.aes_decrypt(<encrypted>, <key>)
```

## Analyze Examples

```python
func.aes_decrypt(get_column(table, 'encrypted_data'), 'secret_key')

┌──────────────┐
│ 'plain text'  │
└──────────────┘
```

## SQL Syntax

```sql
AES_DECRYPT(<encrypted>, <key>)
```

## SQL Examples

```sql
SELECT AES_DECRYPT(encrypted_col, 'secret_key') FROM data;

┌────────────┐
│ plain text  │
└────────────┘
```
