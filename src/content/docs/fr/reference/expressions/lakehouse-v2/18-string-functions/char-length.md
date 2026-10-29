---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH — renvoie le nombre de caractères d'une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

Renvoie le nombre de caractères d'une chaîne.

## Syntaxe Analyze

```python
func.char_length(<str>)
```

## Exemples Analyze

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## Syntaxe SQL

```sql
CHAR_LENGTH(<str>)
```

## Exemples SQL

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
