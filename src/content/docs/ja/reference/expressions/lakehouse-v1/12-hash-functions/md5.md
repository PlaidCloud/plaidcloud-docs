---
title: MD5（Lakehouse v1）
description: MD5 — 文字列のMD5 128ビットチェックサムを計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/md5.md
---

文字列のMD5 128ビットチェックサムを計算します。値は32桁の16進数の文字列として返されます。引数がNULLの場合はNULLが返されます。

## Analyzeの構文

```python
func.md5(<expr>)
```

## Analyzeの例

```python
func.md5('1234567890')

┌──────────────────────────────────────────┐
│ func.md5('1234567890')                   │
├──────────────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f         │
└──────────────────────────────────────────┘
```

## SQLの構文

```sql
MD5(<expr>)
```

## SQLの例

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```
