---
title: LOCATE（Lakehouse v2）
description: LOCATE — 文字列内で部分文字列が最初に現れる位置を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

文字列内で部分文字列が最初に現れる位置を返します。

## Analyze 構文

```python
func.locate(<substr>, <str>[, <pos>])
```

## Analyze の例

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## SQL 構文

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## SQL の例

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
