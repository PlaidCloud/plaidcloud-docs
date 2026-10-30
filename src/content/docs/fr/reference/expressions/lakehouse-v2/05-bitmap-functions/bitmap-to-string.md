---
title: BITMAP_TO_STRING (Lakehouse v2)
description: BITMAP_TO_STRING — convertit un bitmap en chaîne de valeurs séparées par des virgules.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-string.md
---

Convertit un bitmap en chaîne de valeurs séparées par des virgules.

## Syntaxe Analyze

```python
func.bitmap_to_string(<bitmap>)
```

## Exemples Analyze

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## Syntaxe SQL

```sql
BITMAP_TO_STRING(<bitmap>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
