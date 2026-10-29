---
title: POW (Lakehouse v2)
description: POW — devuelve un número elevado a la potencia de otro número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pow.md
---

Devuelve un número elevado a la potencia de otro número.

## Sintaxis de Analyze

```python
func.pow(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.pow(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## Sintaxis de SQL

```sql
POW(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT POW(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
