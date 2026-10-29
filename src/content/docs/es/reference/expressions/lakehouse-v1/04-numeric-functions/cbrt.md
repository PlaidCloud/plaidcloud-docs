---
title: CBRT (Lakehouse v1)
description: CBRT — devuelve la raíz cúbica de un número no negativo x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cbrt.md
---

Devuelve la raíz cúbica de un número no negativo `x`.

## Sintaxis de Analyze

```python
func.cbrt( <x> )
```

## Ejemplos de Analyze

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## Sintaxis de SQL

```sql
CBRT( <x> )
```

## Ejemplos de SQL

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```
