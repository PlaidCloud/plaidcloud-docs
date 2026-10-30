---
title: ADDDATE (Lakehouse v2)
description: ADDDATE — dodaje do daty podany przedział czasu. Alias funkcji `DATE_ADD`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/adddate.md
---

Dodaje do daty podany przedział czasu. Alias funkcji `DATE_ADD`.

## Składnia Analyze

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Przykłady Analyze

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## Składnia SQL

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## Przykłady SQL

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
