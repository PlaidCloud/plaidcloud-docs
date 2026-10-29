---
title: IS_ERROR (Lakehouse v1)
description: IS_ERROR – gibt einen booleschen Wert zurück, der angibt, ob ein Ausdruck ein Fehlerwert ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-error.md
---

Gibt einen booleschen Wert zurück, der angibt, ob ein Ausdruck ein Fehlerwert ist.

Siehe auch: [IS_NOT_ERROR](../is-not-error)

## Analyze-Syntax

```python
func.is_error( <expr> )
```

## Analyze-Beispiele

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

## SQL-Syntax

```sql
IS_ERROR( <expr> )
```

## Rückgabetyp

Gibt `true` zurück, wenn der Ausdruck ein Fehler ist, andernfalls `false`.

## SQL-Beispiele

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
