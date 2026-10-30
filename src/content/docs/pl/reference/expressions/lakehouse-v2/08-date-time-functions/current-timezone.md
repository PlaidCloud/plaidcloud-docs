---
title: CURRENT_TIMEZONE (Lakehouse v2)
description: CURRENT_TIMEZONE — zwraca strefę czasową bieżącej sesji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timezone.md
---

Zwraca strefę czasową bieżącej sesji.

## Składnia Analyze

```python
func.current_timezone()
```

## Przykłady Analyze

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## Składnia SQL

```sql
CURRENT_TIMEZONE()
```

## Przykłady SQL

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```
