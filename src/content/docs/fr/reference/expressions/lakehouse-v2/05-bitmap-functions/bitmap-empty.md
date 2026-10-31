---
title: BITMAP_EMPTY (Lakehouse v2)
description: BITMAP_EMPTY — renvoie un bitmap vide.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-empty.md
---

Renvoie un bitmap vide.

## Syntaxe Analyze

```python
func.bitmap_empty()
```

## Exemples Analyze

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_EMPTY()
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```
