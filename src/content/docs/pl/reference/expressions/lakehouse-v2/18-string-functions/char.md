---
title: CHAR (Lakehouse v2)
description: CHAR — zwraca znak odpowiadający podanemu kodowi ASCII.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char.md
---

Zwraca znak odpowiadający podanemu kodowi ASCII.

## Składnia Analyze

```python
func.char(<code>)
```

## Przykłady Analyze

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## Składnia SQL

```sql
CHAR(<code>)
```

## Przykłady SQL

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```
