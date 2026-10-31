---
title: UCASE（Lakehouse v2）
description: UCASE — 文字列を大文字に変換します。`UPPER` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ucase.md
---

文字列を大文字に変換します。`UPPER` の別名です。

## Analyze 構文

```python
func.ucase(<str>)
```

## Analyze の例

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL 構文

```sql
UCASE(<str>)
```

## SQL の例

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
