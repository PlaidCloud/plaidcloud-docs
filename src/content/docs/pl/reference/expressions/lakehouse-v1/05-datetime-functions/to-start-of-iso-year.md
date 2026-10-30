---
title: TO_START_OF_ISO_YEAR (Lakehouse v1)
description: TO_START_OF_ISO_YEAR — zwraca pierwszy dzień roku ISO dla daty lub daty z czasem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-iso-year.md
---

Zwraca pierwszy dzień roku ISO dla daty lub daty z czasem (znacznik czasu/datetime).

## Składnia Analyze

```python
func.to_start_of_iso_year(<expr>)
```

## Przykłady Analyze

```python
func.to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_iso_year('2023-11-12 09:38:18.165575')        │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-01-02                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_START_OF_ISO_YEAR(<expr>)
```

## Argumenty

| Argumenty | Opis                |
|-----------|---------------------|
| `<expr>`  | data/znacznik czasu |

## Zwracany typ

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT
  to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ to_start_of_iso_year('2023-11-12 09:38:18.165575') │
│                        Date                        │
├────────────────────────────────────────────────────┤
│ 2023-01-02                                         │
└────────────────────────────────────────────────────┘
```
