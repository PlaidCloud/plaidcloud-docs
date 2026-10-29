---
title: NOW (Lakehouse v2)
description: NOW — zwraca bieżącą datę i godzinę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

Zwraca bieżącą datę i godzinę.

## Składnia Analyze

```python
func.now()
```

## Przykłady Analyze

```python
func.now()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
NOW()
```

## Przykłady SQL

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
