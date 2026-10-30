---
title: TO_START_OF_YEAR (Lakehouse v1)
description: TO_START_OF_YEAR — zwraca pierwszy dzień roku dla daty lub daty z czasem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-year.md
---

Zwraca pierwszy dzień roku dla daty lub daty z czasem (timestamp/datetime).

## Składnia Analyze

```python
func.to_start_of_year(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_year('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-01-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_YEAR(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Typ zwracany

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT
  to_start_of_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_year('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-01-01                                     │
└────────────────────────────────────────────────┘
```
