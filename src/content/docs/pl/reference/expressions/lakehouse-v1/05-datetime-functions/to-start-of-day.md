---
title: TO_START_OF_DAY (Lakehouse v1)
description: TO_START_OF_DAY — zaokrągla w dół datę z czasem (znacznik czasu/datetime) do początku dnia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-day.md
---

Zaokrągla w dół datę z czasem (znacznik czasu/datetime) do początku dnia.

## Składnia Analyze

```python
func.to_start_of_day(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_day('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_start_of_day('2023-11-12 09:38:18.165575') │
│                     Timestamp                      │
├────────────────────────────────────────────────────┤
│ 2023-11-12 00:00:00                                │
└────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_DAY( <expr> )
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | znacznik czasu |

## Zwracany typ

`TIMESTAMP`, zwraca datę w formacie „YYYY-MM-DD hh:mm:ss.ffffff”.

## Przykłady SQL

```sql
SELECT
  to_start_of_day('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────┐
│ to_start_of_day('2023-11-12 09:38:18.165575') │
│                   Timestamp                   │
├───────────────────────────────────────────────┤
│ 2023-11-12 00:00:00                           │
└───────────────────────────────────────────────┘
```
