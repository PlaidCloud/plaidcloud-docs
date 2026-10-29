---
title: SHA2 (Lakehouse v1)
description: SHA2 — calcule la famille de fonctions de hachage SHA-2 (SHA-224, SHA-256, SHA-384 et SHA-512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha2.md
---

Calcule la famille de fonctions de hachage SHA-2 (SHA-224, SHA-256, SHA-384 et SHA-512). Si la longueur de hachage ne fait pas partie des valeurs autorisées, la valeur renvoyée est NULL. Sinon, le résultat de la fonction est une valeur de hachage contenant le nombre de bits souhaité, sous la forme d'une chaîne de chiffres hexadécimaux.

## Syntaxe Analyze

```python
func.sha2(<expr>, <expr>)
```

## Exemples Analyze

```python
func.sha2('1234567890', 0)

┌──────────────────────────────────────────────────────────────────┐
│ func.sha2('1234567890', 0))                                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
SHA2(<expr>, <expr>)
```

## Exemples SQL

```sql
SELECT SHA2('1234567890', 0);

┌──────────────────────────────────────────────────────────────────┐
│                       sha2('1234567890', 0)                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```
