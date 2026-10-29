---
title: MD5SUM_NUMERIC (Lakehouse v2)
description: MD5SUM_NUMERIC — 複数の文字列の MD5 ハッシュを、128 ビットの数値として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum-numeric.md
---

複数の文字列の MD5 ハッシュを、128 ビットの数値として返します。

## Analyzeの構文

```python
func.md5sum_numeric(<str1>[, <str2>, ...])
```

## Analyzeの例

```python
func.md5sum_numeric('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQLの構文

```sql
MD5SUM_NUMERIC(<str1>[, <str2>, ...])
```

## SQLの例

```sql
SELECT MD5SUM_NUMERIC('hello');

┌─────────────────────────────────────────┐
│ 268224579284945131320661290344218476706  │
└─────────────────────────────────────────┘
```
