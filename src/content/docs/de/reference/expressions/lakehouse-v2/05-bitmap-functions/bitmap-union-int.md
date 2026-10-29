---
title: BITMAP_UNION_INT (Lakehouse v2)
description: BITMAP_UNION_INT – gibt die Anzahl der eindeutigen Ganzzahlwerte zurück (Aggregat).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-int.md
---

Gibt die Anzahl der eindeutigen Ganzzahlwerte zurück (Aggregat).

## Analyze-Syntax

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Analyze-Beispiele

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## SQL-Syntax

```sql
BITMAP_UNION_INT(<id>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
