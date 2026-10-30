---
title: RAND(n) (Lakehouse v1)
description: RAND(n) — renvoie une valeur aléatoire à virgule flottante v telle que 0 &lt;= v &lt; 1.0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/randn.md
---

Renvoie une valeur aléatoire à virgule flottante v telle que 0 &lt;= v &lt; 1.0. Pour obtenir un entier aléatoire R tel que i &lt;= R &lt; j, utilisez l'expression FLOOR(i + RAND() * (j − i)). L'argument `n` sert de valeur d'initialisation (seed). Pour des valeurs d'argument identiques, RAND(n) renvoie toujours la même valeur et produit donc une séquence de valeurs de colonne reproductible.

## Syntaxe Analyze

```python
func.rand( <n>)
```

## Exemples Analyze

```python
func.rand(1)

┌────────────────────┐
│    func.rand(1)    │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```

## Syntaxe SQL

```sql
RAND( <n>)
```

## Exemples SQL

```sql
SELECT RAND(1);

┌────────────────────┐
│       rand(1)      │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```
