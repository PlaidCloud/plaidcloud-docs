---
title: CONVERT_TZ (Lakehouse v2)
description: CONVERT_TZ — konwertuje datę i godzinę z jednej strefy czasowej na inną.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/convert-tz.md
---

Konwertuje datę i godzinę z jednej strefy czasowej na inną.

## Składnia Analyze

```python
func.convert_tz(<datetime>, <from_tz>, <to_tz>)
```

## Przykłady Analyze

```python
func.convert_tz('2024-01-01 12:00:00', 'UTC', 'America/New_York')

┌───────────────────────┐
│ '2024-01-01 07:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
CONVERT_TZ(<datetime>, <from_tz>, <to_tz>)
```

## Przykłady SQL

```sql
SELECT CONVERT_TZ('2024-01-01 12:00:00', 'UTC', 'America/New_York');

┌─────────────────────┐
│ 2024-01-01 07:00:00  │
└─────────────────────┘
```
