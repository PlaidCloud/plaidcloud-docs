---
title: DIVIDE (Lakehouse v2)
description: DIVIDE — devuelve el resultado de dividir un número entre otro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

Devuelve el resultado de dividir un número entre otro.

## Sintaxis de Analyze

```python
func.divide(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## Sintaxis de SQL

```sql
DIVIDE(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```
