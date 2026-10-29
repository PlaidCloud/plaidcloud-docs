---
title: IS_NOT_NULL (Lakehouse v1)
description: IS_NOT_NULL — comprueba si un valor no es NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-null.md
---

Comprueba si un valor no es NULL.

## Sintaxis de Analyze

```python
func.is_not_null(<expr>)
```

## Ejemplos de Analyze

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
IS_NOT_NULL(<expr>)
```

## Ejemplos de SQL

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
