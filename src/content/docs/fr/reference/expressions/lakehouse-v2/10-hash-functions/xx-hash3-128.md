---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 — renvoie le hachage xxHash3 sur 128 bits d'une valeur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-128.md
---

Renvoie le hachage xxHash3 sur 128 bits d'une valeur.

## Syntaxe Analyze

```python
func.xx_hash3_128(<expr>[, ...])
```

## Exemples Analyze

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Syntaxe SQL

```sql
XX_HASH3_128(<expr>[, ...])
```

## Exemples SQL

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
