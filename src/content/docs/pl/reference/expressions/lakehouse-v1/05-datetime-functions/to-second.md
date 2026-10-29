---
title: TO_SECOND (Lakehouse v1)
description: TO_SECOND — konwertuje datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer sekundy w minucie (0–59).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-second.md
---

Konwertuje datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer sekundy w minucie (0–59).

## Składnia Analyze

```python
func.to_second(<expr>)
```

## Przykłady Analyze

```python
func.to_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_second('2023-11-12 09:38:18.165575') │
│                   UInt8                      │
├──────────────────────────────────────────────┤
│                                           18 │
└──────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_SECOND(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | znacznik czasu |

## Zwracany typ

`TINYINT`

## Przykłady SQL

```sql
SELECT
    to_second('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_second('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      18 │
└─────────────────────────────────────────┘
```
