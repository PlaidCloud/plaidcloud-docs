---
title: TO_QUARTER (Lakehouse v1)
description: TO_QUARTER — pobiera kwartał (1, 2, 3 lub 4) z podanej daty lub znacznika czasu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-quarter.md
---

Pobiera kwartał (1, 2, 3 lub 4) z podanej daty lub znacznika czasu.

## Składnia Analyze

```python
func.to_quarter(<expr>)
```

## Przykłady Analyze

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_QUARTER( <date_or_time_expr> )
```

## Aliasy

- [QUARTER](../quarter)

## Zwracany typ

Liczba całkowita.

## Przykłady SQL

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```
