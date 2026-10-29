---
title: FPOW (Lakehouse v2)
description: FPOW — alias de `POW`. Voir [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fpow.md
---

Alias de `POW`. Voir [POW](../pow/).

## Syntaxe Analyze

```python
func.fpow(2, 10)
```

## Exemples Analyze

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## Syntaxe SQL

```sql
FPOW(<x>)
```

## Exemples SQL

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
