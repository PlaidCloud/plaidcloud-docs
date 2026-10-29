---
title: REPLACE (Lakehouse v2)
description: REPLACE — remplace toutes les occurrences d'une sous-chaîne par une autre sous-chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/replace.md
---

Remplace toutes les occurrences d'une sous-chaîne par une autre sous-chaîne.

## Syntaxe Analyze

```python
func.replace(<str>, <old>, <new>)
```

## Exemples Analyze

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## Syntaxe SQL

```sql
REPLACE(<str>, <old>, <new>)
```

## Exemples SQL

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
