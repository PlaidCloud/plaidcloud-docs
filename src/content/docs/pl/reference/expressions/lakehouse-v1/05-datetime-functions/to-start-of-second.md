---
title: TO_START_OF_SECOND (Lakehouse v1)
description: TO_START_OF_SECOND — zaokrągla w dół datę z czasem (timestamp/datetime) do początku sekundy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-second.md
---

Zaokrągla w dół datę z czasem (timestamp/datetime) do początku sekundy.

## Składnia Analyze

```python
func.to_start_of_second(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_second('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_second('2023-11-12 09:38:18.165575')          │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:38:18                                            │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_SECOND(<expr>)
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
  to_start_of_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ to_start_of_second('2023-11-12 09:38:18.165575') │
│                     Timestamp                    │
├──────────────────────────────────────────────────┤
│ 2023-11-12 09:38:18                              │
└──────────────────────────────────────────────────┘
```
