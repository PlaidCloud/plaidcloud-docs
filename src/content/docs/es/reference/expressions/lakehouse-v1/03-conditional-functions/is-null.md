---
title: IS_NULL (Lakehouse v1)
description: IS_NULL — comprueba si un valor es NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-null.md
---

Comprueba si un valor es NULL.

## Sintaxis de Analyze

```python
func.is_null(<expr>)
```

## Ejemplos de Analyze

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## Sintaxis de SQL

```sql
IS_NULL(<expr>)
```

## Ejemplos de SQL

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```
