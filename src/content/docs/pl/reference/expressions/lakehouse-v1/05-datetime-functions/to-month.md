---
title: TO_MONTH (Lakehouse v1)
description: TO_MONTH — konwertuje datę lub datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer miesiąca.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-month.md
---

Konwertuje datę lub datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer miesiąca (1–12).

## Składnia Analyze

```python
func.to_month(<expr>)
```

## Przykłady Analyze

```python
func.now(), func.to_month(func.now()), func.month(func.now())

┌─────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_month(func.now()) │ func.month(func.now()) │
├────────────────────────────┼───────────────────────────┼────────────────────────┤
│ 2024-03-14 23:34:02.161291 │                         3 │                      3 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_MONTH(<expr>)
```

## Argumenty

| Argumenty | Opis                |
|-----------|---------------------|
| `<expr>`  | data/znacznik czasu |

## Aliasy

- [MONTH](../month)

## Zwracany typ

 `TINYINT`

## Przykłady SQL

```sql
SELECT NOW(), TO_MONTH(NOW()), MONTH(NOW());

┌─────────────────────────────────────────────────────────────┐
│            now()           │ to_month(now()) │ month(now()) │
├────────────────────────────┼─────────────────┼──────────────┤
│ 2024-03-14 23:34:02.161291 │               3 │            3 │
└─────────────────────────────────────────────────────────────┘
```
