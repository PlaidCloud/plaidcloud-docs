---
title: MD5 (Lakehouse v1)
description: MD5 — calcule une somme de contrôle MD5 de 128 bits pour une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/md5.md
---

Calcule une somme de contrôle MD5 de 128 bits pour une chaîne. La valeur est renvoyée sous la forme d'une chaîne de 32 chiffres hexadécimaux, ou NULL si l'argument est NULL.

## Syntaxe Analyze

```python
func.md5(<expr>)
```

## Exemples Analyze

```python
func.md5('1234567890')

┌──────────────────────────────────────────┐
│ func.md5('1234567890')                   │
├──────────────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f         │
└──────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
MD5(<expr>)
```

## Exemples SQL

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```
