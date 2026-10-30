---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL — 正規表現パターンに一致するすべての部分文字列を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract-all.md
---

正規表現パターンに一致するすべての部分文字列を抽出します。

## Analyzeの構文

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Analyzeの例

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## SQLの構文

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## SQLの例

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
