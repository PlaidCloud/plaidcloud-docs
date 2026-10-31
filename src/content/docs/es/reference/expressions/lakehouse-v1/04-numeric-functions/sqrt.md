---
title: SQRT (Lakehouse v1)
description: SQRT — devuelve la raíz cuadrada de un número no negativo x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

Devuelve la raíz cuadrada de un número no negativo `x`. Devuelve Nan para una entrada negativa.

## Sintaxis de Analyze

```python
func.sqrt( <x> )
```

## Ejemplos de Analyze

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## Sintaxis de SQL

```sql
SQRT( <x> )
```

## Ejemplos de SQL

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```
