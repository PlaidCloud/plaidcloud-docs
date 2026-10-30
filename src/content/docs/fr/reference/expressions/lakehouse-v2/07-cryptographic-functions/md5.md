---
title: MD5 (Lakehouse v2)
description: MD5 — renvoie le hachage MD5 d'une chaîne sous forme de chaîne hexadécimale de 32 caractères.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

Renvoie le hachage MD5 d'une chaîne sous forme de chaîne hexadécimale de 32 caractères.

## Syntaxe Analyze

```python
func.md5(<str>)
```

## Exemples Analyze

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## Syntaxe SQL

```sql
MD5(<str>)
```

## Exemples SQL

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
