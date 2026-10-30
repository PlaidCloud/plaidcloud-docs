---
title: TO_BITMAP (Lakehouse v2)
description: TO_BITMAP — convertit une valeur entière en bitmap contenant cette seule valeur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/to-bitmap.md
---

Convertit une valeur entière en bitmap contenant cette seule valeur.

## Syntaxe Analyze

```python
func.to_bitmap(<value>)
```

## Exemples Analyze

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
TO_BITMAP(<value>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
