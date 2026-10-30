---
title: REGEXP_SPLIT（Lakehouse v2）
description: REGEXP_SPLIT — 正規表現パターンで文字列を分割し、部分文字列の配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/regexp-split.md
---

正規表現パターンで文字列を分割し、部分文字列の配列を返します。

## Analyze 構文

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Analyze の例

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## SQL 構文

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## SQL の例

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```
