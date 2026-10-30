---
title: PERCENTILE_DISC_LC (Lakehouse v2)
description: PERCENTILE_DISC_LC — renvoie la valeur de percentile à l'aide d'un algorithme optimisé pour les faibles cardinalités.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc-lc.md
---

Renvoie la valeur de percentile à l'aide d'un algorithme optimisé pour les faibles cardinalités.

## Syntaxe Analyze

```python
func.percentile_disc_lc(0.5)
```

## Exemples Analyze

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## Syntaxe SQL

```sql
PERCENTILE_DISC_LC(0.5)
```

## Exemples SQL

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
