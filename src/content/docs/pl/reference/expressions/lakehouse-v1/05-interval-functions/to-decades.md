---
title: TO_DECADES (Lakehouse v1)
description: TO_DECADES — konwertuje podaną liczbę dekad na typ Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-decades.md
---

Konwertuje podaną liczbę dekad na typ Interval.

- Akceptuje jako dane wejściowe dodatnie liczby całkowite, zero i ujemne liczby całkowite.

## Składnia Analyze

```python
func.to_decades(<decades>)
```

## Przykłady Analyze

```python
func.to_decades(2)
┌──────────────────────────────────────────────────────┐
│ func.to_decades(2)                                   │
├──────────────────────────────────────────────────────┤
│ 20 years                                             │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_DECADES(<decades>)
```

## Typ zwracany

Interval (wyrażony w latach).

## Przykłady SQL

```sql
SELECT TO_DECADES(2), TO_DECADES(0), TO_DECADES((- 2));

┌─────────────────────────────────────────────────┐
│ to_decades(2) │ to_decades(0) │ to_decades(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 20 years      │ 00:00:00      │ -20 years       │
└─────────────────────────────────────────────────┘
```
