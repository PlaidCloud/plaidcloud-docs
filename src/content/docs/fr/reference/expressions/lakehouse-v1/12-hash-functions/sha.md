---
title: SHA (Lakehouse v1)
description: SHA — calcule une somme de contrôle SHA-1 de 160 bits pour la chaîne, comme décrit dans la RFC 3174 (Secure Hash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha.md
---

Calcule une somme de contrôle SHA-1 de 160 bits pour la chaîne, comme décrit dans la RFC 3174 (Secure Hash Algorithm). La valeur est renvoyée sous la forme d'une chaîne de 40 chiffres hexadécimaux, ou NULL si l'argument est NULL.

## Syntaxe Analyze

```python
func.sha(<expr>)
```

## Exemples Analyze

```python
func.sha('1234567890')

┌──────────────────────────────────────────┐
│ func.sha('1234567890')                   │
├──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└──────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
SHA(<expr>)
```

## Alias

- [SHA1](../sha1)

## Exemples SQL

```sql
SELECT SHA('1234567890'), SHA1('1234567890');

┌─────────────────────────────────────────────────────────────────────────────────────┐
│             sha('1234567890')            │            sha1('1234567890')            │
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
