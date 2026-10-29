---
title: TIME_TO_SEC (Lakehouse v2)
description: TIME_TO_SEC — konwertuje wartość czasu na sekundy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-to-sec.md
---

Konwertuje wartość czasu na sekundy.

## Składnia Analyze

```python
func.time_to_sec(<time>)
```

## Przykłady Analyze

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## Składnia SQL

```sql
TIME_TO_SEC(<time>)
```

## Przykłady SQL

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
