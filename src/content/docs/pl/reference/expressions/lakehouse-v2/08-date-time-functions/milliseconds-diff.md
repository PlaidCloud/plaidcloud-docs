---
title: MILLISECONDS_DIFF (Lakehouse v2)
description: MILLISECONDS_DIFF — zwraca liczbę milisekund między dwiema datami i godzinami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/milliseconds-diff.md
---

Zwraca liczbę milisekund między dwiema datami i godzinami.

## Składnia Analyze

```python
func.milliseconds_diff(<end>, <start>)
```

## Przykłady Analyze

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## Składnia SQL

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## Przykłady SQL

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```
