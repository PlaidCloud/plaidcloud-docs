---
title: UTC_TIME (Lakehouse v2)
description: UTC_TIME — zwraca bieżący czas UTC.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-time.md
---

Zwraca bieżący czas UTC.

## Składnia Analyze

```python
func.utc_time()
```

## Przykłady Analyze

```python
func.utc_time()

┌────────────┐
│ '18:30:00'  │
└────────────┘
```

## Składnia SQL

```sql
UTC_TIME()
```

## Przykłady SQL

```sql
SELECT UTC_TIME();

┌──────────┐
│ 18:30:00  │
└──────────┘
```
