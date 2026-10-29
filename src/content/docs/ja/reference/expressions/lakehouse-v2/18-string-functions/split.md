---
title: SPLIT（Lakehouse v2）
description: SPLIT — 区切り文字で文字列を分割し、配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split.md
---

区切り文字で文字列を分割し、配列を返します。

## Analyze 構文

```python
func.split(<str>, <delimiter>)
```

## Analyze の例

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## SQL 構文

```sql
SPLIT(<str>, <delimiter>)
```

## SQL の例

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
