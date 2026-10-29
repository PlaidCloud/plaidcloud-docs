---
title: TO_YYYYMMDDHHMMSS (Lakehouse v1)
description: TO_YYYYMMDDHHMMSS — konwertuje datę lub datę z czasem (timestamp/datetime) na liczbę UInt64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhhmmss.md
---

Konwertuje datę lub datę z czasem (timestamp/datetime) na liczbę UInt64 zawierającą rok, miesiąc, dzień, godzinę, minutę i sekundę (YYYY * 10000000000 + MM * 100000000 + DD * 1000000 + hh * 10000 + mm * 100 + ss).

## Składnia Analyze

```python
func.to_yyyymmddhhmmss(<expr>)
```

## Przykłady Analyze

```python
func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────────┐
│ func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                   UInt64                             │
├──────────────────────────────────────────────────────┤
│                                       20231112092818 │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_YYYYMMDDHHMMSS(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Typ zwracany

`BIGINT`, zwraca wartość w formacie `YYYYMMDDhhmmss`.

## Przykłady SQL

```sql
SELECT
  to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                      UInt64                     │
├─────────────────────────────────────────────────┤
│                                  20231112092818 │
└─────────────────────────────────────────────────┘
```
