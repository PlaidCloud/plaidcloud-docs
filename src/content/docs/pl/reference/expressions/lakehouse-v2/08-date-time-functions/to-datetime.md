---
title: TO_DATETIME (Lakehouse v2)
description: TO_DATETIME — konwertuje wartość na datę i godzinę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime.md
---

Konwertuje wartość na datę i godzinę.

## Składnia Analyze

```python
func.to_datetime(<expr>)
```

## Przykłady Analyze

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
TO_DATETIME(<expr>)
```

## Przykłady SQL

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
