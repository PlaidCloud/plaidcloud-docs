---
title: REGEXP_REPLACE (Lakehouse v2)
description: "PlaidCloud LakehouseでREGEXP_REPLACEパターンマッチング関数を使用します。正規表現パターンに一致する部分文字列を、置換文字列に置き換えます。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

正規表現パターンに一致する部分文字列を、置換文字列に置き換えます。

## Analyzeの構文

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Analyzeの例

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQLの構文

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## SQLの例

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
