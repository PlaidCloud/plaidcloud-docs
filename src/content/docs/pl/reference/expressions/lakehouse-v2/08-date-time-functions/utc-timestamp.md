---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP — zwraca bieżącą datę i godzinę UTC.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

Zwraca bieżącą datę i godzinę UTC.

## Składnia Analyze

```python
func.utc_timestamp()
```

## Przykłady Analyze

```python
func.utc_timestamp()

┌───────────────────────┐
│ '2024-06-15 18:30:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
UTC_TIMESTAMP()
```

## Przykłady SQL

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```
