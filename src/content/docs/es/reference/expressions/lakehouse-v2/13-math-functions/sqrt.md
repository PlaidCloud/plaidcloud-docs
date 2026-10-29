---
title: SQRT (Lakehouse v2)
description: SQRT — devuelve la raíz cuadrada de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sqrt.md
---

Devuelve la raíz cuadrada de un número.

## Sintaxis de Analyze

```python
func.sqrt(<x>)
```

## Ejemplos de Analyze

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## Sintaxis de SQL

```sql
SQRT(<x>)
```

## Ejemplos de SQL

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```
