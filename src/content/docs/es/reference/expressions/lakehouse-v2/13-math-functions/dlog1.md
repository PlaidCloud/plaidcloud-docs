---
title: DLOG1 (Lakehouse v2)
description: DLOG1 — alias de `LN`. Consulte [LN](../ln/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog1.md
---

Alias de `LN`. Consulte [LN](../ln/).

## Sintaxis de Analyze

```python
func.dlog1(2.718281828459045)
```

## Ejemplos de Analyze

```python
func.dlog1(2.718281828459045)

┌─────┐
│ 1.0 │
└─────┘
```

## Sintaxis de SQL

```sql
DLOG1(<x>)
```

## Ejemplos de SQL

```sql
SELECT DLOG1(2.718281828459045);

┌─────┐
│ 1.0 │
└─────┘
```
