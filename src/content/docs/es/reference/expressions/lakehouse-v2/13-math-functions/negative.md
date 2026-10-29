---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — devuelve la negación de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

Devuelve la negación de un número.

## Sintaxis de Analyze

```python
func.negative(<x>)
```

## Ejemplos de Analyze

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## Sintaxis de SQL

```sql
NEGATIVE(<x>)
```

## Ejemplos de SQL

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
