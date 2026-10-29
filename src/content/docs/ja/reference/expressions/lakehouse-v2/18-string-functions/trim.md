---
title: TRIM（Lakehouse v2）
description: TRIM — 文字列の先頭と末尾にある空白または指定した文字を削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/trim.md
---

文字列の先頭と末尾にある空白または指定した文字を削除します。

## Analyze 構文

```python
func.trim(<str>)
```

## Analyze の例

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 構文

```sql
TRIM(<str>)
```

## SQL の例

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
