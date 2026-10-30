---
title: PMOD (Lakehouse v2)
description: PMOD — devuelve el módulo positivo de dividir dos números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

Devuelve el módulo positivo de dividir dos números.

## Sintaxis de Analyze

```python
func.pmod(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## Sintaxis de SQL

```sql
PMOD(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```
