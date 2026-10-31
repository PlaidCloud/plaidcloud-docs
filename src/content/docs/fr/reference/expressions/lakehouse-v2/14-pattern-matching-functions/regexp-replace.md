---
title: REGEXP_REPLACE (Lakehouse v2)
description: "Utilisez la fonction de correspondance de motifs REGEXP_REPLACE dans PlaidCloud Lakehouse. Remplace les sous-chaînes correspondant à un motif d'expression régulière par une chaîne de remplacement."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

Remplace les sous-chaînes correspondant à un motif d'expression régulière par une chaîne de remplacement.

## Syntaxe Analyze

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Exemples Analyze

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## Syntaxe SQL

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## Exemples SQL

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
