---
title: DROUND (Lakehouse v2)
description: DROUND — alias de `ROUND`. Consulte [ROUND](../round/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dround.md
---

Alias de `ROUND`. Consulte [ROUND](../round/).

## Sintaxis de Analyze

```python
func.dround(3.14159, 2)
```

## Ejemplos de Analyze

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## Sintaxis de SQL

```sql
DROUND(<x>)
```

## Ejemplos de SQL

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```
