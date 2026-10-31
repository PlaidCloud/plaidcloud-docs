---
title: SHA2 (Lakehouse v2)
description: SHA2 — renvoie le hachage SHA-2 d'une chaîne pour une longueur en bits donnée (224, 256, 384 ou 512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sha2.md
---

Renvoie le hachage SHA-2 d'une chaîne pour une longueur en bits donnée (224, 256, 384 ou 512).

## Syntaxe Analyze

```python
func.sha2(<str>, <bit_length>)
```

## Exemples Analyze

```python
func.sha2('hello', 256)

┌───────────────┐
│ '2cf24dba...'  │
└───────────────┘
```

## Syntaxe SQL

```sql
SHA2(<str>, <bit_length>)
```

## Exemples SQL

```sql
SELECT SHA2('hello', 256);

┌──────────────────────────────────────────────────────────────────┐
│ 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  │
└──────────────────────────────────────────────────────────────────┘
```
