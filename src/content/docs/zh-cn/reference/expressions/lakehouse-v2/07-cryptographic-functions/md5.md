---
title: MD5 (Lakehouse v2)
description: MD5：以 32 个字符的十六进制字符串形式返回字符串的 MD5 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

以 32 个字符的十六进制字符串形式返回字符串的 MD5 哈希。

## Analyze 语法

```python
func.md5(<str>)
```

## Analyze 示例

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## SQL 语法

```sql
MD5(<str>)
```

## SQL 示例

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
