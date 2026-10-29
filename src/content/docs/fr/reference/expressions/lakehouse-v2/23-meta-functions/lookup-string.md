---
title: LOOKUP_STRING (Lakehouse v2)
description: LOOKUP_STRING — recherche une chaîne dans un dictionnaire et renvoie l'ID correspondant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/lookup-string.md
---

Recherche une chaîne dans un dictionnaire et renvoie l'ID correspondant.

## Syntaxe Analyze

```python
func.lookup_string(<dict_table>, <value>)
```

## Exemples Analyze

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## Exemples SQL

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
