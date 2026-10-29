---
title: SUBDATE (Lakehouse v2)
description: SUBDATE — odejmuje przedział czasu od daty. Alias funkcji `DATE_SUB`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/subdate.md
---

Odejmuje przedział czasu od daty. Alias funkcji `DATE_SUB`.

## Składnia Analyze

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Przykłady Analyze

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## Składnia SQL

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## Przykłady SQL

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```
