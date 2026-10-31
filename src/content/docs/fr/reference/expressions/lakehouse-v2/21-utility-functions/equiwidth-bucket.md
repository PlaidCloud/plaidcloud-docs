---
title: EQUIWIDTH_BUCKET (Lakehouse v2)
description: "Utilisez la fonction utilitaire EQUIWIDTH_BUCKET dans PlaidCloud Lakehouse. Renvoie le numéro de tranche d'une valeur dans un histogramme à largeur égale. Divise la plage [min, max] en intervalles de largeur égale."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/equiwidth-bucket.md
---

Renvoie le numéro de tranche d'une valeur dans un histogramme à largeur égale. Divise la plage [min, max] en intervalles de largeur égale.

## Syntaxe Analyze

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Exemples Analyze

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## Syntaxe SQL

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## Exemples SQL

```sql
SELECT score, EQUIWIDTH_BUCKET(score, 0, 100, 10) AS bucket
FROM students;

┌───────┬────────┐
│ score │ bucket │
├───────┼────────┤
│    25 │      3 │
│    75 │      8 │
│    95 │     10 │
└───────┴────────┘
```
