---
title: REGEXP_SPLIT (Lakehouse v2)
description: REGEXP_SPLIT — découpe une chaîne selon un motif d'expression régulière et renvoie un tableau de sous-chaînes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/regexp-split.md
---

Découpe une chaîne selon un motif d'expression régulière et renvoie un tableau de sous-chaînes.

## Syntaxe Analyze

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Exemples Analyze

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## Syntaxe SQL

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## Exemples SQL

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```
