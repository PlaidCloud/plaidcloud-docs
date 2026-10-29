---
title: BUILD_BITMAP (Lakehouse v1)
description: BUILD_BITMAP – wandelt ein Array positiver ganzer Zahlen in einen BITMAP-Wert um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/build-bitmap.md
---

Wandelt ein Array positiver ganzer Zahlen in einen BITMAP-Wert um.


## Analyze-Syntax

```python
func.build_bitmap( <expr> )
```

## Analyze-Beispiele

```python
func.to_string(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.to_string(func.build_bitmap([1, 4, 5]))  │
├───────────────────────────────────────────────┤
│ 1,4,5                                         │
└───────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BUILD_BITMAP( <expr> )
```

## SQL-Beispiele

```sql
SELECT BUILD_BITMAP([1,4,5])::String;

┌─────────────────────────────────┐
│ build_bitmap([1, 4, 5])::string │
├─────────────────────────────────┤
│ 1,4,5                           │
└─────────────────────────────────┘
```
