---
title: INTERSECT_COUNT (Lakehouse v2)
description: "Utilisez la fonction bitmap INTERSECT_COUNT dans PlaidCloud Lakehouse. Renvoie le nombre d'éléments de l'intersection de plusieurs bitmaps filtrés par dimension."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/intersect-count.md
---

Renvoie le nombre d'éléments de l'intersection de plusieurs bitmaps filtrés par dimension.

## Syntaxe Analyze

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Exemples Analyze

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## Syntaxe SQL

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## Exemples SQL

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
