---
title: MD5SUM (Lakehouse v2)
description: MD5SUM：返回多个字符串拼接后的 MD5 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum.md
---

返回多个字符串拼接后的 MD5 哈希。

## Analyze 语法

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Analyze 示例

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## SQL 语法

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## SQL 示例

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
