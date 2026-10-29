---
title: DCEIL (Lakehouse v2)
description: DCEIL — alias de `CEIL`. Consulte [CEIL](../ceil/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dceil.md
---

Alias de `CEIL`. Consulte [CEIL](../ceil/).

## Sintaxe de Analyze

```python
func.dceil(3.2)
```

## Exemplos de Analyze

```python
func.dceil(3.2)

┌───┐
│ 4 │
└───┘
```

## Sintaxe SQL

```sql
DCEIL(<x>)
```

## Exemplos SQL

```sql
SELECT DCEIL(3.2);

┌───┐
│ 4 │
└───┘
```
