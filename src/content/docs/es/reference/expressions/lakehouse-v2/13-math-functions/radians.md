---
title: RADIANS (Lakehouse v2)
description: RADIANS — convierte grados en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/radians.md
---

Convierte grados en radianes.

## Sintaxis de Analyze

```python
func.radians(<x>)
```

## Ejemplos de Analyze

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## Sintaxis de SQL

```sql
RADIANS(<x>)
```

## Ejemplos de SQL

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
