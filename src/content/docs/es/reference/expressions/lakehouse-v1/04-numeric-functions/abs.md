---
title: ABS (Lakehouse v1)
description: ABS — devuelve el valor absoluto de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/abs.md
---

Devuelve el valor absoluto de `x`.

## Sintaxis de Analyze

```python
func.abs( <x> )
```

## Ejemplos de Analyze

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## Sintaxis de SQL

```sql
ABS( <x> )
```

## Ejemplos de SQL

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
