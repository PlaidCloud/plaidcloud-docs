---
title: NULL_OR_EMPTY (Lakehouse v2)
description: NULL_OR_EMPTY — prüft, ob eine Zeichenfolge NULL oder leer ist. Gibt 1 zurück, wenn dies zutrifft, andernfalls 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/null-or-empty.md
---

Prüft, ob eine Zeichenfolge NULL oder leer ist. Gibt 1 zurück, wenn dies zutrifft, andernfalls 0.

## Analyze-Syntax

```python
func.null_or_empty(<str>)
```

## Analyze-Beispiele

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
NULL_OR_EMPTY(<str>)
```

## SQL-Beispiele

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```
