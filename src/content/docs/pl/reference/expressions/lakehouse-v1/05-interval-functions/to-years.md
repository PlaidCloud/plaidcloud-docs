---
title: TO_YEARS (Lakehouse v1)
description: TO_YEARS — konwertuje podaną liczbę lat na typ Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-years.md
---

Konwertuje podaną liczbę lat na typ Interval.

- Akceptuje jako dane wejściowe dodatnie liczby całkowite, zero i ujemne liczby całkowite.

## Składnia Analyze

```python
func.to_years(<years>)
```

## Przykłady Analyze

```python
func.to_years(2)
┌──────────────────────────────────────────────────────┐
│ func.to_years(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2 years                                              │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_YEARS(<years>)
```

## Typ zwracany

Interval (wyrażony w latach).

## Przykłady SQL

```sql
SELECT TO_YEARS(2), TO_YEARS(0), TO_YEARS((- 2));

┌───────────────────────────────────────────┐
│ to_years(2) │ to_years(0) │ to_years(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2 years     │ 00:00:00    │ -2 years      │
└───────────────────────────────────────────┘
```
