---
title: ATAN (Lakehouse v2)
description: ATAN — devuelve la arcotangente de un número en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

Devuelve la arcotangente de un número en radianes.

## Sintaxis de Analyze

```python
func.atan(<x>)
```

## Ejemplos de Analyze

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## Sintaxis de SQL

```sql
ATAN(<x>)
```

## Ejemplos de SQL

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
