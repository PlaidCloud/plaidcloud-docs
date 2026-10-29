---
title: TO_START_OF_TEN_MINUTES (Lakehouse v1)
description: TO_START_OF_TEN_MINUTES — zaokrągla w dół datę z czasem (timestamp/datetime) do początku dziesięciominutowego przedziału.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-ten-minutes.md
---

Zaokrągla w dół datę z czasem (timestamp/datetime) do początku dziesięciominutowego przedziału.

## Składnia Analyze

```python
func.to_start_of_ten_minutes(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')     │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_TEN_MINUTES(<expr>)
```

## Argumenty

| Argumenty | Opis      |
|-----------|-----------|
| `<expr>`  | timestamp |

## Typ zwracany

`TIMESTAMP`, zwraca datę w formacie „YYYY-MM-DD hh:mm:ss.ffffff”.

## Przykłady SQL

```sql
SELECT
  to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────────┐
│ to_start_of_ten_minutes('2023-11-12 09:38:18.165575') │
│                       Timestamp                       │
├───────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                   │
└───────────────────────────────────────────────────────┘
```
