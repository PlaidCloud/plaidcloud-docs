---
title: BLAKE3 (Lakehouse v1)
description: BLAKE3 — calcule une somme de contrôle BLAKE3 de 256 bits pour une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/blake3.md
---

Calcule une somme de contrôle BLAKE3 de 256 bits pour une chaîne. La valeur est renvoyée sous la forme d'une chaîne de 64 chiffres hexadécimaux, ou NULL si l'argument est NULL.

## Syntaxe Analyze

```python
func.blake3(<expr>)
```

## Exemples Analyze

```python
func.blake3('1234567890')

┌──────────────────────────────────────────────────────────────────┐
│ func.blake3('1234567890')                                        │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BLAKE3(<expr>)
```

## Exemples SQL

```sql
SELECT BLAKE3('1234567890');

┌──────────────────────────────────────────────────────────────────┐
│                       blake3('1234567890')                       │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```
