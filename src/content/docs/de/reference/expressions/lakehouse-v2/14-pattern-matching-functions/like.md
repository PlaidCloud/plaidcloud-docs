---
title: LIKE (Lakehouse v2)
description: "Verwenden Sie die Mustervergleichsfunktion LIKE in PlaidCloud Lakehouse. Gleicht eine Zeichenfolge mit einem Muster ab, wobei `%` (beliebige Zeichen) und `_` (einzelnes Zeichen) als Platzhalter dienen."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

Gleicht eine Zeichenfolge mit einem Muster ab, wobei `%` (beliebige Zeichen) und `_` (einzelnes Zeichen) als Platzhalter dienen.

## Analyze-Syntax

```python
func.like(<str> LIKE <pattern>)
```

## Analyze-Beispiele

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQL-Syntax

```sql
LIKE(<str> LIKE <pattern>)
```

## SQL-Beispiele

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
