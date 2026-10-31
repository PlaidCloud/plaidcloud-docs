---
title: MOD (Lakehouse v2)
description: MOD — devuelve el resto de dividir dos números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

Devuelve el resto de dividir dos números.

## Sintaxis de Analyze

```python
func.mod(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## Sintaxis de SQL

```sql
MOD(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```
