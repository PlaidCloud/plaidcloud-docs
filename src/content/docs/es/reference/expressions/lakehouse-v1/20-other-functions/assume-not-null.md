---
title: ASSUME_NOT_NULL (Lakehouse v1)
description: ASSUME_NOT_NULL produce un valor equivalente no Nullable para un tipo Nullable.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/assume-not-null.md
---

Produce un valor equivalente no `Nullable` para un tipo Nullable. Si el valor original es `NULL`, el resultado es indeterminado. 

## Sintaxis de Analyze

```python
func.assume_not_null(<x>)
```

## Ejemplos de Analyze

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

## Sintaxis de SQL

```sql
ASSUME_NOT_NULL(<x>)
```

## Alias

- [REMOVE_NULLABLE](../remove-nullable)

## Tipo de retorno

Devuelve el tipo de dato original a partir del tipo no `Nullable`; para un tipo `Nullable`, devuelve el tipo de dato no `Nullable` que contiene.

## Ejemplos de SQL

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
