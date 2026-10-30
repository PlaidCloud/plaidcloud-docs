---
title: FLOOR (Lakehouse v1)
description: FLOOR — redondea el número hacia abajo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/floor.md
---

Redondea el número hacia abajo.

## Sintaxis de Analyze

```python
func.floor( <x> )
```

## Ejemplos de Analyze

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## Sintaxis de SQL

```sql
FLOOR( <x> )
```

## Ejemplos de SQL

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```
