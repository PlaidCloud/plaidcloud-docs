---
title: TO_START_OF_WEEK (Lakehouse v1)
description: TO_START_OF_WEEK — zwraca pierwszy dzień tygodnia dla daty lub daty z czasem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-week.md
---

Zwraca pierwszy dzień tygodnia dla daty lub daty z czasem (timestamp/datetime).
Pierwszym dniem tygodnia może być niedziela lub poniedziałek, co określa argument `mode`.

## Składnia Analyze

```python
func.to_start_of_week(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_week('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_WEEK(<expr> [, mode])
```

## Argumenty

| Argumenty | Opis                                                                                                          |
|-----------|---------------------------------------------------------------------------------------------------------------|
| `<expr>`  | data/timestamp                                                                                                |
| `[mode]`  | Opcjonalny. Jeśli wynosi 0, wynikiem jest niedziela, w przeciwnym razie wynikiem jest poniedziałek. Wartość domyślna to 0 |

## Typ zwracany

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT
  to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_week('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-11-12                                     │
└────────────────────────────────────────────────┘
```
