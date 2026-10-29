---
title: MD5 (Lakehouse v2)
description: MD5 — 文字列の MD5 ハッシュを、32 文字の 16 進数文字列として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

文字列の MD5 ハッシュを、32 文字の 16 進数文字列として返します。

## Analyzeの構文

```python
func.md5(<str>)
```

## Analyzeの例

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## SQLの構文

```sql
MD5(<str>)
```

## SQLの例

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
