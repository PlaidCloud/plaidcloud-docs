---
title: RAND() (Lakehouse v1)
description: RAND() — renvoie une valeur aléatoire à virgule flottante v comprise entre 0 <= v < 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/rand.md
---

Renvoie une valeur aléatoire à virgule flottante v telle que 0 &lt;= v &lt; 1.0. Pour obtenir un entier aléatoire R tel que i &lt;= R &lt; j, utilisez l'expression FLOOR(i + RAND() * (j − i)).

## Syntaxe Analyze

```python
func.rand()
```

## Exemples Analyze

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## Syntaxe SQL

```sql
RAND()
```

## Exemples SQL

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
