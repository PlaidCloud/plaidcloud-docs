---
title: BIN (Lakehouse v2)
description: BIN — renvoie la représentation binaire, sous forme de chaîne, d'un entier.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

Renvoie la représentation binaire, sous forme de chaîne, d'un entier.

## Syntaxe Analyze

```python
func.bin(<x>)
```

## Exemples Analyze

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## Syntaxe SQL

```sql
BIN(<x>)
```

## Exemples SQL

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
