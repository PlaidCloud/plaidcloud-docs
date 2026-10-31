---
title: ATAN (Lakehouse v1)
description: ATAN — devuelve la arcotangente de x, es decir, el valor cuya tangente es x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan.md
---

Devuelve la arcotangente de `x`, es decir, el valor cuya tangente es `x`.

## Sintaxis de Analyze

```python
func.atan( <x> )
```

## Ejemplos de Analyze

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
ATAN( <x> )
```

## Ejemplos de SQL

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```
