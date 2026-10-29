---
title: TAN (Lakehouse v2)
description: TAN — devuelve la tangente de un número en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tan.md
---

Devuelve la tangente de un número en radianes.

## Sintaxis de Analyze

```python
func.tan(<x>)
```

## Ejemplos de Analyze

```python
func.tan(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Sintaxis de SQL

```sql
TAN(<x>)
```

## Ejemplos de SQL

```sql
SELECT TAN(0);

┌─────┐
│ 0.0  │
└─────┘
```
