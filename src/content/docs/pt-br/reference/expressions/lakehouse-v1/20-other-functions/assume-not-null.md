---
title: ASSUME_NOT_NULL (Lakehouse v1)
description: ASSUME_NOT_NULL — resulta em um valor equivalente não anulável para um tipo anulável.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/assume-not-null.md
---

Resulta em um valor equivalente não `Nullable` para um tipo Nullable. Se o valor original for `NULL`, o resultado é indeterminado. 

## Sintaxe no Analyze

```python
func.assume_not_null(<x>)
```

## Exemplos no Analyze

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

## Sintaxe SQL

```sql
ASSUME_NOT_NULL(<x>)
```

## Aliases

- [REMOVE_NULLABLE](../remove-nullable)

## Tipo de retorno

Retorna o tipo de dados original a partir do tipo não `Nullable`; retorna o tipo de dados não `Nullable` incorporado para o tipo `Nullable`.

## Exemplos de SQL

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
