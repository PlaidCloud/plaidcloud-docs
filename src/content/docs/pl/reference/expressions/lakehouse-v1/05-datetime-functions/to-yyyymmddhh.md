---
title: TO_YYYYMMDDHH (Lakehouse v1)
description: TO_YYYYMMDDHH — formatuje podaną datę lub timestamp do postaci tekstowej w formacie „YYYYMMDDHH”.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhh.md
---

Formatuje podaną datę lub timestamp do postaci tekstowej w formacie „YYYYMMDDHH” (rok, miesiąc, dzień, godzina).

## Składnia Analyze

```python
func.to_yyyymmddhh(<expr>)
```

## Przykłady Analyze

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_YYYYMMDDHH(<expr>)
```

## Argumenty

| Argumenty | Opis          |
|-----------|---------------|
| `<expr>`  | data/datetime |

## Typ zwracany

Zwraca 64-bitową liczbę całkowitą bez znaku (UInt64) w formacie „YYYYMMDDHH”.

## Przykłady SQL

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```
