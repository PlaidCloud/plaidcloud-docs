---
title: BITMAP_TO_BINARY (Lakehouse v2)
description: BITMAP_TO_BINARY — convertit un bitmap en valeur binaire.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-binary.md
---

Convertit un bitmap en valeur binaire.

## Syntaxe Analyze

```python
func.bitmap_to_binary(<bitmap>)
```

## Exemples Analyze

```python
func.bitmap_to_binary(get_column(table, 'bm'))

┌──────────┐
│ (binary) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_TO_BINARY(<bitmap>)
```

## Exemples SQL

```sql
SELECT HEX(BITMAP_TO_BINARY(BITMAP_FROM_STRING('1,2,3')));

┌──────────────┐
│ (hex string) │
└──────────────┘
```
