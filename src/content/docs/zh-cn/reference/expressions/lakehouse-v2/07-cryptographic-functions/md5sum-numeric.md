---
title: MD5SUM_NUMERIC (Lakehouse v2)
description: MD5SUM_NUMERIC：以 128 位数值形式返回多个字符串的 MD5 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum-numeric.md
---

以 128 位数值形式返回多个字符串的 MD5 哈希。

## Analyze 语法

```python
func.md5sum_numeric(<str1>[, <str2>, ...])
```

## Analyze 示例

```python
func.md5sum_numeric('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL 语法

```sql
MD5SUM_NUMERIC(<str1>[, <str2>, ...])
```

## SQL 示例

```sql
SELECT MD5SUM_NUMERIC('hello');

┌─────────────────────────────────────────┐
│ 268224579284945131320661290344218476706  │
└─────────────────────────────────────────┘
```
