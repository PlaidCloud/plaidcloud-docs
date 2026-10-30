---
title: TO_START_OF_MINUTE (Lakehouse v1)
description: TO_START_OF_MINUTE — zaokrągla w dół datę z czasem (znacznik czasu/datetime) do początku minuty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-minute.md
---

Zaokrągla w dół datę z czasem (znacznik czasu/datetime) do początku minuty.

## Składnia Analyze

```python
func.to_start_of_minute(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_minute('2023-11-12 09:38:18.165575')          │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:38:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_MINUTE( <expr> )
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
  to_start_of_minute('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ to_start_of_minute('2023-11-12 09:38:18.165575') │
│                     Timestamp                    │
├──────────────────────────────────────────────────┤
│ 2023-11-12 09:38:00                              │
└──────────────────────────────────────────────────┘
```
