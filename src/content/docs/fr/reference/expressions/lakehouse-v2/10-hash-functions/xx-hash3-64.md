---
title: XX_HASH3_64 (Lakehouse v2)
description: XX_HASH3_64 — renvoie le hachage xxHash3 sur 64 bits d'une valeur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-64.md
---

Renvoie le hachage xxHash3 sur 64 bits d'une valeur.

## Syntaxe Analyze

```python
func.xx_hash3_64(<expr>[, ...])
```

## Exemples Analyze

```python
func.xx_hash3_64('hello')

┌──────────┐
│ (bigint)  │
└──────────┘
```

## Syntaxe SQL

```sql
XX_HASH3_64(<expr>[, ...])
```

## Exemples SQL

```sql
SELECT XX_HASH3_64('hello');

┌──────────────────────┐
│ -7685981735718036227  │
└──────────────────────┘
```
