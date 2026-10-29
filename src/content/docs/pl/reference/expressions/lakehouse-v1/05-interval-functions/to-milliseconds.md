---
title: TO_MILLISECONDS (Lakehouse v1)
description: TO_MILLISECONDS — konwertuje podaną liczbę milisekund na typ Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-milliseconds.md
---

Konwertuje podaną liczbę milisekund na typ Interval.

- Akceptuje jako dane wejściowe dodatnie liczby całkowite, zero i ujemne liczby całkowite.

## Składnia Analyze

```python
func.to_milliseconds(<milliseconds>)
```

## Przykłady Analyze

```python
func.to_milliseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_milliseconds(2)                              │
├──────────────────────────────────────────────────────┤
│  0:00:00.002                                         │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_MILLISECONDS(<milliseconds>)
```

## Typ zwracany

Interval (w formacie `hh:mm:ss.sss`).

## Przykłady SQL

```sql
SELECT TO_MILLISECONDS(2), TO_MILLISECONDS(0), TO_MILLISECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_milliseconds(2) │ to_milliseconds(0) │ to_milliseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.002        │ 00:00:00           │ -0:00:00.002         │
└────────────────────────────────────────────────────────────────┘
```
