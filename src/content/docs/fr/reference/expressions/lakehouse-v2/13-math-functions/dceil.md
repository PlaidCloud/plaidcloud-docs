---
title: DCEIL (Lakehouse v2)
description: DCEIL — alias de `CEIL`. Voir [CEIL](../ceil/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dceil.md
---

Alias de `CEIL`. Voir [CEIL](../ceil/).

## Syntaxe Analyze

```python
func.dceil(3.2)
```

## Exemples Analyze

```python
func.dceil(3.2)

┌───┐
│ 4 │
└───┘
```

## Syntaxe SQL

```sql
DCEIL(<x>)
```

## Exemples SQL

```sql
SELECT DCEIL(3.2);

┌───┐
│ 4 │
└───┘
```
