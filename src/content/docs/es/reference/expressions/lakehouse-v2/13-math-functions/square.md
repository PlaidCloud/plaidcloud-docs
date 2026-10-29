---
title: SQUARE (Lakehouse v2)
description: SQUARE — devuelve el cuadrado de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

Devuelve el cuadrado de un número.

## Sintaxis de Analyze

```python
func.square(<x>)
```

## Ejemplos de Analyze

```python
func.square(7)

┌────┐
│ 49  │
└────┘
```

## Sintaxis de SQL

```sql
SQUARE(<x>)
```

## Ejemplos de SQL

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```
