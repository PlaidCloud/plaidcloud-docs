---
title: ATAN2 (Lakehouse v2)
description: ATAN2 — devuelve la arcotangente de y/x, usando los signos para determinar el cuadrante.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan2.md
---

Devuelve la arcotangente de y/x, usando los signos para determinar el cuadrante.

## Sintaxis de Analyze

```python
func.atan2(<y>, <x>)
```

## Ejemplos de Analyze

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## Sintaxis de SQL

```sql
ATAN2(<y>, <x>)
```

## Ejemplos de SQL

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
