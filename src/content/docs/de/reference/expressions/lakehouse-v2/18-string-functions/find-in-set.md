---
title: FIND_IN_SET (Lakehouse v2)
description: FIND_IN_SET — gibt die Position einer Zeichenfolge in einer durch Kommas getrennten Liste zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/find-in-set.md
---

Gibt die Position einer Zeichenfolge in einer durch Kommas getrennten Liste zurück.

## Analyze-Syntax

```python
func.find_in_set(<str>, <strlist>)
```

## Analyze-Beispiele

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## SQL-Syntax

```sql
FIND_IN_SET(<str>, <strlist>)
```

## SQL-Beispiele

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```
