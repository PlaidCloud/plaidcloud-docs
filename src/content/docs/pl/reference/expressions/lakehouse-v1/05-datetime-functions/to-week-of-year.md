---
title: TO_WEEK_OF_YEAR (Lakehouse v1)
description: TO_WEEK_OF_YEAR — oblicza numer tygodnia w roku dla podanej daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-week-of-year.md
---

Oblicza numer tygodnia w roku dla podanej daty.

Numeracja tygodni ISO działa następująco: 4 stycznia zawsze należy do pierwszego tygodnia. Jeśli 1 stycznia przypada w czwartek, tydzień od poniedziałku 29 grudnia do niedzieli 4 stycznia jest tygodniem 1 według ISO. Jeśli 1 stycznia przypada w piątek, tydzień od poniedziałku 4 stycznia do niedzieli 10 stycznia jest tygodniem 1 według ISO.

## Składnia Analyze

```python
func.to_week_of_year(<expr>)
```

## Przykłady Analyze

```python
func.now(), func.to_week_of_year(func.now()), func.week(func.now()), func.weekofyear(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_week_of_year(func.now()) │ func.week(func.now()) │ func.weekofyear(func.now()) │
├────────────────────────────┼──────────────────────────────────┼───────────────────────┼─────────────────────────────┤
│ 2024-03-14 23:30:04.011624 │                               11 │                    11 │                          11 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_WEEK_OF_YEAR(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Aliasy

- [WEEK](../week)
- [WEEKOFYEAR](../weekofyear)

## Typ zwracany

Zwraca liczbę całkowitą oznaczającą numer tygodnia w roku, w zakresie od 1 do 53.

## Przykłady SQL

```sql
SELECT NOW(), TO_WEEK_OF_YEAR(NOW()), WEEK(NOW()), WEEKOFYEAR(NOW());

┌───────────────────────────────────────────────────────────────────────────────────────┐
│            now()           │ to_week_of_year(now()) │ week(now()) │ weekofyear(now()) │
├────────────────────────────┼────────────────────────┼─────────────┼───────────────────┤
│ 2024-03-14 23:30:04.011624 │                     11 │          11 │                11 │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
