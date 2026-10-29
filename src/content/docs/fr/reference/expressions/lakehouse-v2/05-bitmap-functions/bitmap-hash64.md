---
title: BITMAP_HASH64 (Lakehouse v2)
description: BITMAP_HASH64 — calcule un hachage 64 bits d'une valeur et renvoie un bitmap contenant ce hachage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash64.md
---

Calcule un hachage 64 bits d'une valeur et renvoie un bitmap contenant ce hachage.

## Syntaxe Analyze

```python
func.bitmap_hash64(<value>)
```

## Exemples Analyze

```python
func.bitmap_hash64('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_HASH64(<value>)
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_HASH64('hello'));

┌───┐
│ 1 │
└───┘
```
