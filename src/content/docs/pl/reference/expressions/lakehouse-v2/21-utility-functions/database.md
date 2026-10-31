---
title: DATABASE (Lakehouse v2)
description: DATABASE — zwraca nazwę bieżącej bazy danych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/database.md
---

Zwraca nazwę bieżącej bazy danych.

## Składnia Analyze

```python
func.database()
```

## Przykłady Analyze

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## Składnia SQL

```sql
DATABASE()
```

## Przykłady SQL

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
