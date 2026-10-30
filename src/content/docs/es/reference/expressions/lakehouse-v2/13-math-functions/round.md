---
title: ROUND (Lakehouse v2)
description: ROUND — redondea un número a un número específico de decimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/round.md
---

Redondea un número a un número específico de decimales.

## Sintaxis de Analyze

```python
func.round(<x>[, <d>])
```

## Ejemplos de Analyze

```python
func.round(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## Sintaxis de SQL

```sql
ROUND(<x>[, <d>])
```

## Ejemplos de SQL

```sql
SELECT ROUND(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
