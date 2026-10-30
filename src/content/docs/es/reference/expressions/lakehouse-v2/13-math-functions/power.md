---
title: POWER (Lakehouse v2)
description: POWER — devuelve un número elevado a la potencia de otro número. Alias de `POW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/power.md
---

Devuelve un número elevado a la potencia de otro número. Alias de `POW`.

## Sintaxis de Analyze

```python
func.power(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.power(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## Sintaxis de SQL

```sql
POWER(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT POWER(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
