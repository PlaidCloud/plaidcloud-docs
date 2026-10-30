---
title: TO_MINUTE (Lakehouse v1)
description: TO_MINUTE — konwertuje datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer minuty w godzinie (0–59).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-minute.md
---

Konwertuje datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer minuty w godzinie (0–59).


## Składnia Analyze

```python
func.to_minute(<expr>)
```

## Przykłady Analyze

```python
func.to_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_minute('2023-11-12 09:38:18.165575')       │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                 38 │
└────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_MINUTE(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | znacznik czasu |

## Zwracany typ

 `TINYINT`

## Przykłady SQL

```sql
SELECT
    to_minute('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_minute('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      38 │
└─────────────────────────────────────────┘
```
