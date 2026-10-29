---
title: LIKE (Lakehouse v2)
description: "PlaidCloud LakehouseでLIKEパターンマッチング関数を使用します。`%`（任意の文字列）と `_`（任意の1文字）を使用して、文字列をパターンと照合します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

`%`（任意の文字列）と `_`（任意の1文字）のワイルドカードを使用して、文字列をパターンと照合します。

## Analyzeの構文

```python
func.like(<str> LIKE <pattern>)
```

## Analyzeの例

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQLの構文

```sql
LIKE(<str> LIKE <pattern>)
```

## SQLの例

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
