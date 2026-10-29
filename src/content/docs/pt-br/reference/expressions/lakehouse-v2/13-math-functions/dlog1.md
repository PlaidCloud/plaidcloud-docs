---
title: DLOG1 (Lakehouse v2)
description: DLOG1 — alias de `LN`. Consulte [LN](../ln/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog1.md
---

Alias de `LN`. Consulte [LN](../ln/).

## Sintaxe do Analyze

```python
func.dlog1(2.718281828459045)
```

## Exemplos do Analyze

```python
func.dlog1(2.718281828459045)

┌─────┐
│ 1.0 │
└─────┘
```

## Sintaxe SQL

```sql
DLOG1(<x>)
```

## Exemplos de SQL

```sql
SELECT DLOG1(2.718281828459045);

┌─────┐
│ 1.0 │
└─────┘
```
