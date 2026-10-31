---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 — renvoie le hachage MurmurHash3 sur 32 bits d'une valeur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/murmur-hash3-32.md
---

Renvoie le hachage MurmurHash3 sur 32 bits d'une valeur.

## Syntaxe Analyze

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Exemples Analyze

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## Syntaxe SQL

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## Exemples SQL

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
