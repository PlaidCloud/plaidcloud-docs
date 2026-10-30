---
title: DPOW (Lakehouse v2)
description: DPOW — alias de `POW`. Voir [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dpow.md
---

Alias de `POW`. Voir [POW](../pow/).

## Syntaxe Analyze

```python
func.dpow(2, 10)
```

## Exemples Analyze

```python
func.dpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## Syntaxe SQL

```sql
DPOW(<x>)
```

## Exemples SQL

```sql
SELECT DPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
