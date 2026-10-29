---
title: CHARACTER_LENGTH (Lakehouse v2)
description: CHARACTER_LENGTH — renvoie le nombre de caractères d'une chaîne. Alias de `CHAR_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/character-length.md
---

Renvoie le nombre de caractères d'une chaîne. Alias de `CHAR_LENGTH`.

## Syntaxe Analyze

```python
func.character_length(<str>)
```

## Exemples Analyze

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## Syntaxe SQL

```sql
CHARACTER_LENGTH(<str>)
```

## Exemples SQL

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
