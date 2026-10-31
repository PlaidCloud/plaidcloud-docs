---
title: TO_MONDAY (Lakehouse v1)
description: TO_MONDAY — zaokrągla w dół datę lub datę z czasem (znacznik czasu/datetime) do najbliższego poniedziałku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-monday.md
---

Zaokrągla w dół datę lub datę z czasem (znacznik czasu/datetime) do najbliższego poniedziałku.
Zwraca datę.

## Składnia Analyze

```python
func.to_monday(<expr>)
```

## Przykłady Analyze

```python
func.to_monday('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_monday('2023-11-12 09:38:18.165575')       │
│                      Date                          │
├────────────────────────────────────────────────────┤
│ 2023-11-06                                         │
└────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_MONDAY(<expr>)
```

## Argumenty

| Argumenty   | Opis        |
| ----------- | ----------- |
| `<expr>` | data/znacznik czasu |

## Zwracany typ

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT
    to_monday('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_monday('2023-11-12 09:38:18.165575') │
│                   Date                  │
├─────────────────────────────────────────┤
│ 2023-11-06                              │
└─────────────────────────────────────────┘
```
