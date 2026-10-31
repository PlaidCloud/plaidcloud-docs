---
title: INTERSECT_COUNT (Lakehouse v2)
description: "Verwenden Sie die Bitmap-Funktion INTERSECT_COUNT in PlaidCloud Lakehouse. Gibt die Anzahl der Elemente in der Schnittmenge mehrerer Bitmaps zurück, gefiltert nach Dimension."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/intersect-count.md
---

Gibt die Anzahl der Elemente in der Schnittmenge mehrerer Bitmaps zurück, gefiltert nach Dimension.

## Analyze-Syntax

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Analyze-Beispiele

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## SQL-Syntax

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## SQL-Beispiele

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
