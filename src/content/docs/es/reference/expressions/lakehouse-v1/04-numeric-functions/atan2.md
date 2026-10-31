---
title: ATAN2 (Lakehouse v1)
description: ATAN2 — devuelve la arcotangente de las dos variables x e y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

Devuelve la arcotangente de las dos variables `x` e `y`. Es similar a calcular la arcotangente de `y` / `x`, salvo que se usan los signos de ambos argumentos para determinar el cuadrante del resultado. `ATAN(y, x)` es sinónimo de `ATAN2(y, x)`.

## Sintaxis de Analyze

```python
func.atan2( <y, x> )
```

## Ejemplos de Analyze

```python
func.atan2((- 2), 2)

┌─────────────────────┐
│ func.atan2((- 2), 2)│
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
ATAN2( <y, x> )
```

## Ejemplos de SQL

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
