---
title: SECONDS_DIFF (Lakehouse v2)
description: SECONDS_DIFF — zwraca liczbę sekund między dwiema datami i godzinami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-diff.md
---

Zwraca liczbę sekund między dwiema datami i godzinami.

## Składnia Analyze

```python
func.seconds_diff(<end>, <start>)
```

## Przykłady Analyze

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## Składnia SQL

```sql
SECONDS_DIFF(<end>, <start>)
```

## Przykłady SQL

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```
