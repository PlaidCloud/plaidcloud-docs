---
title: LENGTH（Lakehouse v2）
description: LENGTH — 文字列の長さをバイト数で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

文字列の長さをバイト数で返します。

## Analyze 構文

```python
func.length(<str>)
```

## Analyze の例

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL 構文

```sql
LENGTH(<str>)
```

## SQL の例

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
