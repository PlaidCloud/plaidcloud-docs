---
title: UPPER（Lakehouse v2）
description: UPPER — 文字列を大文字に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/upper.md
---

文字列を大文字に変換します。

## Analyze 構文

```python
func.upper(<str>)
```

## Analyze の例

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL 構文

```sql
UPPER(<str>)
```

## SQL の例

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
