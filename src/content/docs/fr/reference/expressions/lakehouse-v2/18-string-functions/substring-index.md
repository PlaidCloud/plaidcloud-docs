---
title: SUBSTRING_INDEX (Lakehouse v2)
description: "Utilisez la fonction de chaîne SUBSTRING_INDEX dans PlaidCloud Lakehouse. Renvoie la sous-chaîne située avant ou après un nombre donné d'occurrences d'un délimiteur."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

Renvoie la sous-chaîne située avant ou après un nombre donné d'occurrences d'un délimiteur.

## Syntaxe Analyze

```python
func.substring_index(<str>, <delim>, <count>)
```

## Exemples Analyze

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## Syntaxe SQL

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## Exemples SQL

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
