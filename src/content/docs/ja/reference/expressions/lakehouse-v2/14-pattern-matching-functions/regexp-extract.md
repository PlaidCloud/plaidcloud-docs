---
title: REGEXP_EXTRACT (Lakehouse v2)
description: REGEXP_EXTRACT — 正規表現パターンに一致する最初の部分文字列を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract.md
---

正規表現パターンに一致する最初の部分文字列を抽出します。

## Analyzeの構文

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Analyzeの例

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## SQLの構文

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## SQLの例

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
