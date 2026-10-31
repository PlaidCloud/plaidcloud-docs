---
title: TIME_FORMAT (Lakehouse v2)
description: TIME_FORMAT — formatuje wartość czasu zgodnie z ciągiem formatu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-format.md
---

Formatuje wartość czasu zgodnie z ciągiem formatu.

## Składnia Analyze

```python
func.time_format(<time>, <format>)
```

## Przykłady Analyze

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## Składnia SQL

```sql
TIME_FORMAT(<time>, <format>)
```

## Przykłady SQL

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```
