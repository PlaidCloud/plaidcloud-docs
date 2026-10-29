---
title: LOWER（Lakehouse v2）
description: LOWER — 文字列を小文字に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

文字列を小文字に変換します。

## Analyze 構文

```python
func.lower(<str>)
```

## Analyze の例

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 構文

```sql
LOWER(<str>)
```

## SQL の例

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
