---
title: PI (Lakehouse v1)
description: PI — devuelve el valor de π como un valor de coma flotante.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

Devuelve el valor de π como un valor de coma flotante.

## Sintaxis de Analyze

```python
func.pi()
```

## Ejemplos de Analyze

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## Sintaxis de SQL

```sql
PI()
```

## Ejemplos de SQL

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```
