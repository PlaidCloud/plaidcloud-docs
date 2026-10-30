---
title: TOKENIZE（Lakehouse v2）
description: "PlaidCloud Lakehouse で TOKENIZE 文字列関数を使用します。指定したアナライザーを使って文字列を用語の配列にトークン化します。全文検索に便利です。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

指定したアナライザーを使って文字列を用語の配列にトークン化します。全文検索のシナリオに便利です。

## Analyze 構文

```python
func.tokenize('The quick brown fox', 'english')
```

## Analyze の例

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## SQL 構文

```sql
TOKENIZE(<str>[, <analyzer>])
```

## SQL の例

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
