---
title: SEC_TO_TIME (Lakehouse v2)
description: SEC_TO_TIME — konwertuje sekundy na wartość czasu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/sec-to-time.md
---

Konwertuje sekundy na wartość czasu.

## Składnia Analyze

```python
func.sec_to_time(<seconds>)
```

## Przykłady Analyze

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## Składnia SQL

```sql
SEC_TO_TIME(<seconds>)
```

## Przykłady SQL

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```
