---
title: REGEXP_COUNT (Lakehouse v2)
description: "PlaidCloud LakehouseでREGEXP_COUNTパターンマッチング関数を使用します。文字列内に正規表現パターンが出現する回数を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

文字列内に正規表現パターンが出現する回数を返します。

## Analyzeの構文

```python
func.regexp_count(<str>, <pattern>)
```

## Analyzeの例

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## SQLの構文

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## SQLの例

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
