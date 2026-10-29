---
title: STARTS_WITH（Lakehouse v2）
description: STARTS_WITH — 文字列が指定した接頭辞で始まるかどうかを判定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/starts-with.md
---

文字列が指定した接頭辞で始まるかどうかを判定します。

## Analyze 構文

```python
func.starts_with(<str>, <prefix>)
```

## Analyze の例

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## SQL 構文

```sql
STARTS_WITH(<str>, <prefix>)
```

## SQL の例

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
