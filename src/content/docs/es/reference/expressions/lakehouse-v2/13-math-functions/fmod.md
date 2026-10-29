---
title: FMOD (Lakehouse v2)
description: FMOD — devuelve el resto en coma flotante de dividir dos números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

Devuelve el resto en coma flotante de dividir dos números.

## Sintaxis de Analyze

```python
func.fmod(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## Sintaxis de SQL

```sql
FMOD(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
