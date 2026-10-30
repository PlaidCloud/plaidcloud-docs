---
title: IS_NOT_ERROR (Lakehouse v1)
description: IS_NOT_ERROR — devuelve un valor booleano que indica si una expresión es un valor de error.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-error.md
---

Devuelve un valor booleano que indica si una expresión es un valor de error.

Consulte también: [IS_ERROR](../is-error)

## Sintaxis de Analyze

```python
func.is_error( <expr> )
```

## Ejemplos de Analyze

```python
# Indicates division by zero, hence an error
func.is_error((1 / 0)), func.is_not_error((1 / 0))

┌─────────────────────────────────────────────────────┐
│ func.is_error((1 / 0)) │ func.is_not_error((1 / 0)) │
├────────────────────────┼────────────────────────────┤
│ true                   │ false                      │
└─────────────────────────────────────────────────────┘

# The conversion to DATE is successful, hence not an error
func.is_error(func.to_date('2024-03-17')), func.is_not_error(func.to_date('2024-03-17'))

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_error(func.to_date('2024-03-17')) │ func.is_not_error(func.to_date('2024-03-17')) │
├───────────────────────────────────────────┼───────────────────────────────────────────────┤
│ false                                     │ true                                          │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
IS_NOT_ERROR( <expr> )
```

## Tipo de valor devuelto

Devuelve `true` si la expresión no es un error; de lo contrario, `false`.

## Ejemplos de SQL

```sql
-- Indicates division by zero, hence an error
SELECT IS_ERROR(1/0), IS_NOT_ERROR(1/0);

┌───────────────────────────────────────────┐
│ is_error((1 / 0)) │ is_not_error((1 / 0)) │
├───────────────────┼───────────────────────┤
│ true              │ false                 │
└───────────────────────────────────────────┘

-- The conversion to DATE is successful, hence not an error
SELECT IS_ERROR('2024-03-17'::DATE), IS_NOT_ERROR('2024-03-17'::DATE);

┌─────────────────────────────────────────────────────────────────┐
│ is_error('2024-03-17'::date) │ is_not_error('2024-03-17'::date) │
├──────────────────────────────┼──────────────────────────────────┤
│ false                        │ true                             │
└─────────────────────────────────────────────────────────────────┘
```
