---
title: DLOG1 (Lakehouse v2)
description: DLOG1 — alias de `LN`. Voir [LN](../ln/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog1.md
---

Alias de `LN`. Voir [LN](../ln/).

## Syntaxe Analyze

```python
func.dlog1(2.718281828459045)
```

## Exemples Analyze

```python
func.dlog1(2.718281828459045)

┌─────┐
│ 1.0 │
└─────┘
```

## Syntaxe SQL

```sql
DLOG1(<x>)
```

## Exemples SQL

```sql
SELECT DLOG1(2.718281828459045);

┌─────┐
│ 1.0 │
└─────┘
```
