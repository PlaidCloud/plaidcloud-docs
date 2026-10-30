---
title: TO_BASE64 (Lakehouse v1)
description: TO_BASE64 convertit l'argument de type chaîne en forme encodée base64 et renvoie le résultat sous forme de chaîne de caractères.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

Convertit l'argument de type chaîne en forme encodée base64 et renvoie le résultat sous forme de chaîne de caractères.
Si l'argument n'est pas une chaîne, il est converti en chaîne avant l'encodage.
Le résultat est NULL si l'argument est NULL.

## Syntaxe Analyze

```python
func.to_base64(<v>)
```

## Exemples Analyze

```python
func.to_base64('abc')
┌───────────────────────┐
│ func.to_base64('abc') │
├───────────────────────┤
│ YWJj                  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TO_BASE64(<v>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<v>`     | La valeur.  |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
