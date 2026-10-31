---
title: DPOW (Lakehouse v2)
description: DPOW — alias de `POW`. Consulte [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dpow.md
---

Alias de `POW`. Consulte [POW](../pow/).

## Sintaxis de Analyze

```python
func.dpow(2, 10)
```

## Ejemplos de Analyze

```python
func.dpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## Sintaxis de SQL

```sql
DPOW(<x>)
```

## Ejemplos de SQL

```sql
SELECT DPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
