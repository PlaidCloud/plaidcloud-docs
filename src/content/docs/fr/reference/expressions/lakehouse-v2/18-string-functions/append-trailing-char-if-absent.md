---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "Utilisez la fonction de chaîne APPEND_TRAILING_CHAR_IF_ABSENT dans PlaidCloud Lakehouse. Ajoute un caractère à la fin d'une chaîne s'il n'y figure pas déjà."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

Ajoute un caractère à la fin d'une chaîne s'il n'y figure pas déjà.

## Syntaxe Analyze

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Exemples Analyze

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## Syntaxe SQL

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## Exemples SQL

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
