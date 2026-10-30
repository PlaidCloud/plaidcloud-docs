---
title: DEGREES (Lakehouse v2)
description: DEGREES — convierte radianes en grados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/degrees.md
---

Convierte radianes en grados.

## Sintaxis de Analyze

```python
func.degrees(<x>)
```

## Ejemplos de Analyze

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## Sintaxis de SQL

```sql
DEGREES(<x>)
```

## Ejemplos de SQL

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
