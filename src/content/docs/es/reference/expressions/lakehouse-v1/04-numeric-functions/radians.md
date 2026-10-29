---
title: RADIANS (Lakehouse v1)
description: RADIANS — devuelve el argumento x convertido de grados a radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/radians.md
---

Devuelve el argumento `x` convertido de grados a radianes.

## Sintaxis de Analyze

```python
func.radians( <x> )
```

## Ejemplos de Analyze

```python
func.radians(90)

┌────────────────────┐
│  func.radians(90)  │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
RADIANS( <x> )
```

## Ejemplos de SQL

```sql
SELECT RADIANS(90);

┌────────────────────┐
│     radians(90)    │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```
