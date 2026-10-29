---
title: TO_CENTURIES (Lakehouse v1)
description: TO_CENTURIES — konwertuje podaną liczbę stuleci na typ Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-centuries.md
---

Konwertuje podaną liczbę stuleci na typ Interval.

- Akceptuje jako dane wejściowe dodatnie liczby całkowite, zero i ujemne liczby całkowite.

## Składnia Analyze

```python
func.to_centuries(<centuries>)
```

## Przykłady Analyze

```python
func.to_centuries(2)
┌──────────────────────────────────────────────────────┐
│ func.to_centuries(2)                                 │
├──────────────────────────────────────────────────────┤
│ 200 years                                            │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_CENTURIES(<centuries>)
```

## Typ zwracany

Interval (wyrażony w latach).

## Przykłady SQL

```sql
SELECT TO_CENTURIES(2), TO_CENTURIES(0), TO_CENTURIES(-2);

┌───────────────────────────────────────────────────────┐
│ to_centuries(2) │ to_centuries(0) │ to_centuries(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 200 years       │ 00:00:00        │ -200 years        │
└───────────────────────────────────────────────────────┘
```
