---
title: TO_HOUR (Lakehouse v1)
description: TO_HOUR — konwertuje datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer godziny w formacie 24-godzinnym (0–23).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-hour.md
---

Konwertuje datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer godziny w formacie 24-godzinnym (0–23).
Funkcja zakłada, że jeśli zegary są przesuwane do przodu, następuje to o jedną godzinę o 2:00, a jeśli są cofane, następuje to o jedną godzinę o 3:00 (co nie zawsze jest prawdą — nawet w Moskwie zegary były dwukrotnie przestawiane w różnych momentach).


## Składnia Analyze

```python
func.to_hour(<expr>)
```

## Przykłady Analyze

```python
func.to_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_hour('2023-11-12 09:38:18.165575')         │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  9 │
└────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_HOUR(<expr>)
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
    to_hour('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────┐
│ to_hour('2023-11-12 09:38:18.165575') │
│                 UInt8                 │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘
```
