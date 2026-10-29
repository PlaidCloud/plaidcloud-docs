---
title: TO_START_OF_MONTH (Lakehouse v1)
description: TO_START_OF_MONTH — zaokrągla w dół datę lub datę z czasem (znacznik czasu/datetime) do pierwszego dnia miesiąca.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-month.md
---

Zaokrągla w dół datę lub datę z czasem (znacznik czasu/datetime) do pierwszego dnia miesiąca.
Zwraca datę.

## Składnia Analyze

```python
func.to_start_of_month(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_month('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_month('2023-11-12 09:38:18.165575')           │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_MONTH(<expr>)
```

## Argumenty

| Argumenty | Opis                |
|-----------|---------------------|
| `<expr>`  | data/znacznik czasu |

## Zwracany typ

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT
  to_start_of_month('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_start_of_month('2023-11-12 09:38:18.165575') │
│                       Date                      │
├─────────────────────────────────────────────────┤
│ 2023-11-01                                      │
└─────────────────────────────────────────────────┘
```
