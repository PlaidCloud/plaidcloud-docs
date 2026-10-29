---
title: REGEXP (Lakehouse v2)
description: REGEXP – prüft, ob eine Zeichenfolge einem Muster eines regulären Ausdrucks entspricht.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp.md
---

Prüft, ob eine Zeichenfolge einem Muster eines regulären Ausdrucks entspricht.

## Analyze-Syntax

```python
func.regexp(<str> REGEXP <pattern>)
```

## Analyze-Beispiele

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQL-Syntax

```sql
REGEXP(<str> REGEXP <pattern>)
```

## SQL-Beispiele

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```
