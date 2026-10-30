---
title: BAR (Lakehouse v2)
description: "Utilisez la fonction utilitaire BAR dans PlaidCloud Lakehouse. Renvoie une chaîne représentant visuellement une barre pour une valeur située dans une plage. Utile pour les visualisations en mode texte."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

Renvoie une chaîne représentant visuellement une barre pour une valeur située dans une plage. Utile pour les visualisations en mode texte.

## Syntaxe Analyze

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Exemples Analyze

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## Syntaxe SQL

```sql
BAR(<value>, <min>, <max>, <width>)
```

## Exemples SQL

```sql
SELECT score, BAR(score, 0, 100, 20) AS bar FROM students;

┌───────┬──────────────────────┐
│ score │ bar                  │
├───────┼──────────────────────┤
│    25 │ █████                │
│    50 │ ██████████           │
│    75 │ ███████████████      │
│   100 │ ████████████████████ │
└───────┴──────────────────────┘
```
