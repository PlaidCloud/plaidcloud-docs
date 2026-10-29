---
title: FPOW (Lakehouse v2)
description: FPOW — alias de `POW`. Consulte [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fpow.md
---

Alias de `POW`. Consulte [POW](../pow/).

## Sintaxis de Analyze

```python
func.fpow(2, 10)
```

## Ejemplos de Analyze

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## Sintaxis de SQL

```sql
FPOW(<x>)
```

## Ejemplos de SQL

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
