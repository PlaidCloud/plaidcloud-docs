---
title: REPLACE（Lakehouse v2）
description: REPLACE — 部分文字列に一致するすべての箇所を、別の部分文字列に置換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/replace.md
---

部分文字列に一致するすべての箇所を、別の部分文字列に置換します。

## Analyze 構文

```python
func.replace(<str>, <old>, <new>)
```

## Analyze の例

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## SQL 構文

```sql
REPLACE(<str>, <old>, <new>)
```

## SQL の例

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
