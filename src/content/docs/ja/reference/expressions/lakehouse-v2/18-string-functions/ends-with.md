---
title: ENDS_WITH（Lakehouse v2）
description: ENDS_WITH — 文字列が指定した接尾辞で終わるかどうかを判定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ends-with.md
---

文字列が指定した接尾辞で終わるかどうかを判定します。

## Analyze 構文

```python
func.ends_with(<str>, <suffix>)
```

## Analyze の例

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## SQL 構文

```sql
ENDS_WITH(<str>, <suffix>)
```

## SQL の例

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
