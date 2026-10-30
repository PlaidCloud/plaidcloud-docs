---
title: DATABASE (Lakehouse v1)
description: DATABASE — zwraca nazwę aktualnie wybranej bazy danych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

Zwraca nazwę aktualnie wybranej bazy danych. Jeśli żadna baza danych nie jest wybrana, funkcja zwraca `default`.

## Składnia Analyze

```python
func.database()
```

## Przykłady Analyze

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## Składnia SQL

```sql
DATABASE()
```

## Przykłady SQL

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
