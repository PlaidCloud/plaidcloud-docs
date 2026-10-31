---
title: TO_DAY_OF_MONTH (Lakehouse v1)
description: TO_DAY_OF_MONTH — konwertuje datę lub datę z czasem (znacznik czasu/datetime) na liczbę UInt8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-month.md
---

Konwertuje datę lub datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer dnia miesiąca (1–31).

## Składnia Analyze

```python
func.to_day_of_month(<expr>)
```

## Przykłady Analyze

```python
func.now(), func.to_day_of_month(func.now()), func.day(func.now())

┌──────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_day_of_month(func.now()) │ func.day(func.now()) │
├────────────────────────────┼──────────────────────────────────┼──────────────────────┤
│ 2024-03-14 23:35:41.947962 │                               14 │                   14 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_DAY_OF_MONTH(<expr>)
```

## Argumenty

| Argumenty | Opis                |
|-----------|---------------------|
| `<expr>`  | data/znacznik czasu |

## Aliasy

- [DAY](../day)

## Zwracany typ

`TINYINT`

## Przykłady SQL

```sql
SELECT NOW(), TO_DAY_OF_MONTH(NOW()), DAY(NOW());

┌──────────────────────────────────────────────────────────────────┐
│            now()           │ to_day_of_month(now()) │ day(now()) │
├────────────────────────────┼────────────────────────┼────────────┤
│ 2024-03-14 23:35:41.947962 │                     14 │         14 │
└──────────────────────────────────────────────────────────────────┘
```
