---
title: BITMAP_HASH (Lakehouse v2)
description: BITMAP_HASH — calcule un hachage 32 bits d'une valeur et renvoie un bitmap contenant ce hachage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash.md
---

Calcule un hachage 32 bits d'une valeur et renvoie un bitmap contenant ce hachage.

## Syntaxe Analyze

```python
func.bitmap_hash(<value>)
```

## Exemples Analyze

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_HASH(<value>)
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```
