---
title: TO_MILLENNIA (Lakehouse v1)
description: TO_MILLENNIA — konwertuje podaną liczbę tysiącleci na typ Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-millennia.md
---

Konwertuje podaną liczbę tysiącleci na typ Interval.

- Akceptuje jako dane wejściowe dodatnie liczby całkowite, zero i ujemne liczby całkowite.

## Składnia Analyze

```python
func.to_millennia(<millennia>)
```

## Przykłady Analyze

```python
func.to_millennia(2)
┌──────────────────────────────────────────────────────┐
│ func.to_millennia(2)                                 │
├──────────────────────────────────────────────────────┤
│ 2000 years                                            │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_MILLENNIA(<millennia>)
```

## Typ zwracany

Interval (wyrażony w latach).

## Przykłady SQL

```sql
SELECT TO_MILLENNIA(2), TO_MILLENNIA(0), TO_MILLENNIA((- 2));

┌───────────────────────────────────────────────────────┐
│ to_millennia(2) │ to_millennia(0) │ to_millennia(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 2000 years      │ 00:00:00        │ -2000 years       │
└───────────────────────────────────────────────────────┘
```
