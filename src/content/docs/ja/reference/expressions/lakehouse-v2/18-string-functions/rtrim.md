---
title: RTRIM（Lakehouse v2）
description: RTRIM — 文字列の末尾にある空白または指定した文字を削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rtrim.md
---

文字列の末尾にある空白または指定した文字を削除します。

## Analyze 構文

```python
func.rtrim(<str>)
```

## Analyze の例

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 構文

```sql
RTRIM(<str>)
```

## SQL の例

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```
