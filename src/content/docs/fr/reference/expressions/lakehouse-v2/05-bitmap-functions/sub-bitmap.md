---
title: SUB_BITMAP (Lakehouse v2)
description: SUB_BITMAP — renvoie un sous-bitmap à partir d'une position donnée, avec une limite de cardinalité.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/sub-bitmap.md
---

Renvoie un sous-bitmap à partir d'une position donnée, avec une limite de cardinalité.

## Syntaxe Analyze

```python
func.sub_bitmap(<bitmap>, <offset>, <limit>)
```

## Exemples Analyze

```python
func.sub_bitmap(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
SUB_BITMAP(<bitmap>, <offset>, <limit>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(SUB_BITMAP(BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
