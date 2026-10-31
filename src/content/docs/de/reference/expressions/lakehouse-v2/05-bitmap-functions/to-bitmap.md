---
title: TO_BITMAP (Lakehouse v2)
description: TO_BITMAP – wandelt einen Ganzzahlwert in eine Bitmap um, die nur diesen einen Wert enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/to-bitmap.md
---

Wandelt einen Ganzzahlwert in eine Bitmap um, die nur diesen einen Wert enthält.

## Analyze-Syntax

```python
func.to_bitmap(<value>)
```

## Analyze-Beispiele

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
TO_BITMAP(<value>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
