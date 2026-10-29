---
title: SHA（Lakehouse v1）
description: SHA — RFC 3174（Secure Hash Algorithm）に記載されているSHA-1 160ビットチェックサムを文字列に対して計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha.md
---

RFC 3174（Secure Hash Algorithm）に記載されているSHA-1 160ビットチェックサムを、文字列に対して計算します。値は40桁の16進数の文字列として返されます。引数がNULLの場合はNULLが返されます。

## Analyzeの構文

```python
func.sha(<expr>)
```

## Analyzeの例

```python
func.sha('1234567890')

┌──────────────────────────────────────────┐
│ func.sha('1234567890')                   │
├──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└──────────────────────────────────────────┘
```

## SQLの構文

```sql
SHA(<expr>)
```

## エイリアス

- [SHA1](../sha1)

## SQLの例

```sql
SELECT SHA('1234567890'), SHA1('1234567890');

┌─────────────────────────────────────────────────────────────────────────────────────┐
│             sha('1234567890')            │            sha1('1234567890')            │
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
