---
title: LTRIM（Lakehouse v2）
description: LTRIM — 文字列の先頭にある空白または指定した文字を削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ltrim.md
---

文字列の先頭にある空白または指定した文字を削除します。

## Analyze 構文

```python
func.ltrim(<str>)
```

## Analyze の例

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 構文

```sql
LTRIM(<str>)
```

## SQL の例

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
