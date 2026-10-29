---
title: REGEXP (Lakehouse v2)
description: REGEXP — 文字列が正規表現パターンに一致するかどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp.md
---

文字列が正規表現パターンに一致するかどうかをチェックします。

## Analyzeの構文

```python
func.regexp(<str> REGEXP <pattern>)
```

## Analyzeの例

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQLの構文

```sql
REGEXP(<str> REGEXP <pattern>)
```

## SQLの例

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```
