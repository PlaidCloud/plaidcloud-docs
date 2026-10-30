---
title: XXHASH32 (Lakehouse v1)
description: XXHASH32 — calcule une valeur de hachage xxHash32 de 32 bits pour une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash32.md
---

Calcule une valeur de hachage xxHash32 de 32 bits pour une chaîne. La valeur est renvoyée sous la forme d'un UInt32, ou NULL si l'argument est NULL.

## Syntaxe Analyze

```python
func.xxhash32(<expr>)
```

## Exemples Analyze

```python
func.xxhash32('1234567890')

┌─────────────────────────────┐
│ func.xxhash32('1234567890') │
├─────────────────────────────┤
│                  3896585587 │
└─────────────────────────────┘
```

## Syntaxe SQL

```sql
XXHASH32(<expr>)
```

## Exemples SQL

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```
