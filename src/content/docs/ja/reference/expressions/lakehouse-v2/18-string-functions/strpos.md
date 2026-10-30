---
title: STRPOS（Lakehouse v2）
description: STRPOS — 部分文字列が最初に現れる位置を返します。`LOCATE` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strpos.md
---

部分文字列が最初に現れる位置を返します。`LOCATE` の別名です。

## Analyze 構文

```python
func.strpos(<str>, <substr>)
```

## Analyze の例

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL 構文

```sql
STRPOS(<str>, <substr>)
```

## SQL の例

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
