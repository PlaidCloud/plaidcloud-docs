---
title: LIKE (Lakehouse v2)
description: "Użyj funkcji dopasowywania wzorców LIKE w PlaidCloud Lakehouse. Dopasowuje ciąg znaków do wzorca przy użyciu symboli wieloznacznych `%` (dowolne znaki) i `_` (pojedynczy znak)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

Dopasowuje ciąg znaków do wzorca przy użyciu symboli wieloznacznych `%` (dowolne znaki) i `_` (pojedynczy znak).

## Składnia Analyze

```python
func.like(<str> LIKE <pattern>)
```

## Przykłady Analyze

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## Składnia SQL

```sql
LIKE(<str> LIKE <pattern>)
```

## Przykłady SQL

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
