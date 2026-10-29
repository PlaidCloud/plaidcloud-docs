---
title: LCASE（Lakehouse v2）
description: LCASE — 文字列を小文字に変換します。`LOWER` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lcase.md
---

文字列を小文字に変換します。`LOWER` の別名です。

## Analyze 構文

```python
func.lcase(<str>)
```

## Analyze の例

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 構文

```sql
LCASE(<str>)
```

## SQL の例

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
