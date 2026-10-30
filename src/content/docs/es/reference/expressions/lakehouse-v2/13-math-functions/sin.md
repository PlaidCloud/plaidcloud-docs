---
title: SIN (Lakehouse v2)
description: SIN — devuelve el seno de un número en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

Devuelve el seno de un número en radianes.

## Sintaxis de Analyze

```python
func.sin(<x>)
```

## Ejemplos de Analyze

```python
func.sin(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Sintaxis de SQL

```sql
SIN(<x>)
```

## Ejemplos de SQL

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```
