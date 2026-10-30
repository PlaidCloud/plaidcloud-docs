---
title: MD5SUM (Lakehouse v2)
description: MD5SUM — 連結した複数の文字列の MD5 ハッシュを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum.md
---

連結した複数の文字列の MD5 ハッシュを返します。

## Analyzeの構文

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Analyzeの例

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## SQLの構文

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## SQLの例

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
