---
title: DROUND (Lakehouse v2)
description: DROUND — alias de `ROUND`. Consulte [ROUND](../round/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dround.md
---

Alias de `ROUND`. Consulte [ROUND](../round/).

## Sintaxe de Analyze

```python
func.dround(3.14159, 2)
```

## Exemplos de Analyze

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## Sintaxe SQL

```sql
DROUND(<x>)
```

## Exemplos SQL

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```
