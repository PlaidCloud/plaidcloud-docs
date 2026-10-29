---
title: LENGTH (Lakehouse v1)
description: LENGTH renvoie la longueur d'une chaîne ou d'une valeur binaire donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

Renvoie la longueur d'une chaîne ou d'une valeur binaire donnée. Pour les chaînes, la longueur correspond au nombre de caractères, chaque caractère UTF-8 comptant pour un seul caractère. Pour les données binaires, la longueur correspond au nombre d'octets.

## Syntaxe Analyze

```python
func.length(<expr>)
```

## Exemples Analyze

```python
func.length('Hello')
┌──────────────────────┐
│ func.length('Hello') │
├──────────────────────┤
│                    5 │
└──────────────────────┘
```

## Syntaxe SQL

```sql
LENGTH(<expr>)
```

## Alias

- [CHAR_LENGTH](../char-length)
- [CHARACTER_LENGTH](../character-length)
- [LENGTH_UTF8](../length-utf8)

## Type de retour

BIGINT

## Exemples SQL

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
