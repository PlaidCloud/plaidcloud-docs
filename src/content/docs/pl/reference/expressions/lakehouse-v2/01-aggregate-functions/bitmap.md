---
title: BITMAP (Lakehouse v2)
description: BITMAP — zwraca sumę bitmap dla zbioru wartości. Zwykle używana z BITMAP_AGG.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bitmap.md
---

Zwraca sumę bitmap dla zbioru wartości. Zwykle używana z BITMAP_AGG.

## Składnia Analyze

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Przykłady Analyze

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP(<id>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```
