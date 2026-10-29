---
title: MD5 (Lakehouse v1)
description: MD5：计算字符串的 MD5 128 位校验和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/md5.md
---

计算字符串的 MD5 128 位校验和。返回值为 32 个十六进制数字组成的字符串；如果参数为 NULL，则返回 NULL。

## Analyze 语法

```python
func.md5(<expr>)
```

## Analyze 示例

```python
func.md5('1234567890')

┌──────────────────────────────────────────┐
│ func.md5('1234567890')                   │
├──────────────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f         │
└──────────────────────────────────────────┘
```

## SQL 语法

```sql
MD5(<expr>)
```

## SQL 示例

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```
