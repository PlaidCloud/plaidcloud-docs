---
title: CURRENT_TIMESTAMP (Lakehouse v2)
description: CURRENT_TIMESTAMP — zwraca bieżącą datę i godzinę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timestamp.md
---

Zwraca bieżącą datę i godzinę.

## Składnia Analyze

```python
func.current_timestamp()
```

## Przykłady Analyze

```python
func.current_timestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
CURRENT_TIMESTAMP()
```

## Przykłady SQL

```sql
SELECT CURRENT_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
