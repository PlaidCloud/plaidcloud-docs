---
title: TOKENIZE (Lakehouse v2)
description: "Utilisez la fonction de chaîne TOKENIZE dans PlaidCloud Lakehouse. Découpe une chaîne en un tableau de termes à l'aide de l'analyseur spécifié. Utile pour la recherche en texte intégral."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

Découpe une chaîne en un tableau de termes à l'aide de l'analyseur spécifié. Utile dans les scénarios de recherche en texte intégral.

## Syntaxe Analyze

```python
func.tokenize('The quick brown fox', 'english')
```

## Exemples Analyze

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
TOKENIZE(<str>[, <analyzer>])
```

## Exemples SQL

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
