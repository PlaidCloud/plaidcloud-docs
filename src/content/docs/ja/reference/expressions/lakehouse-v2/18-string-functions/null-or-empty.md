---
title: NULL_OR_EMPTY（Lakehouse v2）
description: NULL_OR_EMPTY — 文字列が NULL または空であるかどうかを判定します。該当する場合は 1、そうでない場合は 0 を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/null-or-empty.md
---

文字列が NULL または空であるかどうかを判定します。該当する場合は 1、そうでない場合は 0 を返します。

## Analyze 構文

```python
func.null_or_empty(<str>)
```

## Analyze の例

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## SQL 構文

```sql
NULL_OR_EMPTY(<str>)
```

## SQL の例

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```
