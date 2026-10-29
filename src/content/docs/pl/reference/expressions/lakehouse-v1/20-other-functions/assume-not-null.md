---
title: ASSUME_NOT_NULL (Lakehouse v1)
description: ASSUME_NOT_NULL — zwraca równoważną wartość niedopuszczającą NULL dla typu dopuszczającego NULL (Nullable).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/assume-not-null.md
---

Zwraca równoważną wartość niedopuszczającą NULL (`Nullable`) dla typu Nullable. Jeśli oryginalna wartość to `NULL`, wynik jest nieokreślony. 

## Składnia Analyze

```python
func.assume_not_null(<x>)
```

## Przykłady Analyze

```python
With a table like:

┌────────────────────┐
│        x  │   y    │
├────────────────────┤
│         1 │   NULL │
│         2 │      3 │
└────────────────────┘

func.assume_not_null(y)
┌─────────────────────────┐
│ func.assume_not_null(y) │
├─────────────────────────┤
│                       0 │
│                       3 │
└─────────────────────────┘
```

## Składnia SQL

```sql
ASSUME_NOT_NULL(<x>)
```

## Aliasy

- [REMOVE_NULLABLE](../remove-nullable)

## Zwracany typ

Dla typu niebędącego `Nullable` zwraca oryginalny typ danych; dla typu `Nullable` zwraca zawarty w nim typ danych niebędący `Nullable`.

## Przykłady SQL

```sql
CREATE TABLE default.t_null ( x int,  y int null);

INSERT INTO default.t_null values (1, null), (2, 3);

SELECT ASSUME_NOT_NULL(y), REMOVE_NULLABLE(y) FROM t_null;

┌─────────────────────────────────────────┐
│ assume_not_null(y) │ remove_nullable(y) │
├────────────────────┼────────────────────┤
│                  0 │                  0 │
│                  3 │                  3 │
└─────────────────────────────────────────┘
```
