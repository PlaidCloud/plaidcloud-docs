---
title: TO_YYYYMMDD (Lakehouse v1)
description: TO_YYYYMMDD — konwertuje datę lub datę z czasem (timestamp/datetime) na liczbę UInt32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmdd.md
---

Konwertuje datę lub datę z czasem (timestamp/datetime) na liczbę UInt32 zawierającą rok, miesiąc i dzień (YYYY * 10000 + MM * 100 + DD).

## Składnia Analyze

```python
func.to_yyyymmdd(<expr>)
```

## Przykłady Analyze

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_YYYYMMDD(<expr>)
```

## Argumenty

| Argumenty | Opis          |
|-----------|---------------|
| `<expr>`  | data/datetime |

## Typ zwracany

`INT`, zwraca wartość w formacie `YYYYMMDD`.

## Przykłady SQL

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```
