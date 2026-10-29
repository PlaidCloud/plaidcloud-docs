---
title: TO_START_OF_QUARTER (Lakehouse v1)
description: TO_START_OF_QUARTER — zaokrągla w dół datę lub datę z czasem (timestamp/datetime) do pierwszego dnia kwartału.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-quarter.md
---

Zaokrągla w dół datę lub datę z czasem (timestamp/datetime) do pierwszego dnia kwartału.
Pierwszym dniem kwartału jest 1 stycznia, 1 kwietnia, 1 lipca lub 1 października.
Zwraca datę.

## Składnia Analyze

```python
func.to_start_of_quarter(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_QUARTER(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`   | data/timestamp |

## Typ zwracany

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```
