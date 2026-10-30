---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME — zwraca bieżący czas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-time.md
---

Zwraca bieżący czas.

## Składnia Analyze

```python
func.current_time()
```

## Przykłady Analyze

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## Składnia SQL

```sql
CURRENT_TIME()
```

## Przykłady SQL

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
