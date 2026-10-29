---
title: POSITIVE (Lakehouse v2)
description: POSITIVE — devuelve el valor sin cambios (más unario).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

Devuelve el valor sin cambios (más unario).

## Sintaxis de Analyze

```python
func.positive(<x>)
```

## Ejemplos de Analyze

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## Sintaxis de SQL

```sql
POSITIVE(<x>)
```

## Ejemplos de SQL

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```
