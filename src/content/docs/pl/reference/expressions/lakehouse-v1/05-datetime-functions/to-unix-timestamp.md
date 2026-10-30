---
title: TO_UNIX_TIMESTAMP (Lakehouse v1)
description: TO_UNIX_TIMESTAMP — konwertuje timestamp w formacie daty i czasu na format znacznika czasu Uniksa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-unix-timestamp.md
---

Konwertuje timestamp w formacie daty i czasu na format znacznika czasu Uniksa. Znacznik czasu Uniksa to liczba sekund, które upłynęły od 1 stycznia 1970 r., godz. 00:00:00 UTC.

## Składnia Analyze

```python
func.to_unix_timestamp(<expr>)
```

## Przykłady Analyze

```python
func.to_unix_timestamp('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_unix_timestamp('2023-11-12 09:38:18.165575')           │
│                          UInt32                                │
├────────────────────────────────────────────────────────────────┤
│                                                     1699781898 │
└────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_UNIX_TIMESTAMP(<expr>)
```

## Argumenty

| Argumenty   | Opis                |
| ----------- | ------------------- |
| `<expr>`    | Timestamp           |

Więcej informacji o typie danych timestamp znajdziesz w sekcji Data i czas.

## Typ zwracany

`BIGINT`

## Przykłady SQL

```sql
SELECT
  to_unix_timestamp('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_unix_timestamp('2023-11-12 09:38:18.165575') │
│                      UInt32                     │
├─────────────────────────────────────────────────┤
│                                      1699781898 │
└─────────────────────────────────────────────────┘
```
