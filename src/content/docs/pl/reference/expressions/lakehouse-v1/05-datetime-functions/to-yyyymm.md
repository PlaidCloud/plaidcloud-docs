---
title: TO_YYYYMM (Lakehouse v1)
description: TO_YYYYMM — konwertuje datę lub datę z czasem (timestamp/datetime) na liczbę UInt32 zawierającą rok i miesiąc.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymm.md
---

Konwertuje datę lub datę z czasem (timestamp/datetime) na liczbę UInt32 zawierającą numer roku i miesiąca.

## Składnia Analyze

```python
func.to_yyyymm(<expr>)
```

## Przykłady Analyze

```python
func.to_yyyymm('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_yyyymm('2023-11-12 09:38:18.165575') │
│                   UInt32                     │
├──────────────────────────────────────────────┤
│                                       202311 │
└──────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_YYYYMM(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Typ zwracany

`INT`, zwraca wartość w formacie `YYYYMM`.

## Przykłady SQL

```sql
SELECT
  to_yyyymm('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_yyyymm('2023-11-12 09:38:18.165575') │
│                  UInt32                 │
├─────────────────────────────────────────┤
│                                  202311 │
└─────────────────────────────────────────┘
```
