---
title: XXHASH64 (Lakehouse v1)
description: XXHASH64 — calcule une valeur de hachage xxHash64 de 64 bits pour une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash64.md
---

Calcule une valeur de hachage xxHash64 de 64 bits pour une chaîne. La valeur est renvoyée sous la forme d'un UInt64, ou NULL si l'argument est NULL.

## Syntaxe Analyze

```python
func.xxhash64(<expr>)
```

## Exemples Analyze

```python
func.xxhash64('1234567890')

┌─────────────────────────────┐
│ func.xxhash64('1234567890') │
├─────────────────────────────┤
│        12237639266330420150 │
└─────────────────────────────┘
```

## Syntaxe SQL

```sql
XXHASH64(<expr>)
```

## Exemples SQL

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```
