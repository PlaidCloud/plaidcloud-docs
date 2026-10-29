---
title: REGEXP_COUNT (Lakehouse v2)
description: "Utilisez la fonction de correspondance de motifs REGEXP_COUNT dans PlaidCloud Lakehouse. Renvoie le nombre d'occurrences d'un motif d'expression régulière dans une chaîne."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

Renvoie le nombre d'occurrences d'un motif d'expression régulière dans une chaîne.

## Syntaxe Analyze

```python
func.regexp_count(<str>, <pattern>)
```

## Exemples Analyze

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## Syntaxe SQL

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## Exemples SQL

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
