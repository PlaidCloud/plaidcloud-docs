---
title: DROUND (Lakehouse v2)
description: DROUND — alias de `ROUND`. Voir [ROUND](../round/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dround.md
---

Alias de `ROUND`. Voir [ROUND](../round/).

## Syntaxe Analyze

```python
func.dround(3.14159, 2)
```

## Exemples Analyze

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## Syntaxe SQL

```sql
DROUND(<x>)
```

## Exemples SQL

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```
