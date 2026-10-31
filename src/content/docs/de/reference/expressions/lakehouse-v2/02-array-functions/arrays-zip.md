---
title: ARRAYS_ZIP (Lakehouse v2)
description: ARRAYS_ZIP – führt mehrere Arrays zu einem Array aus Structs zusammen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-zip.md
---

Führt mehrere Arrays zu einem Array aus Structs zusammen.

## Analyze-Syntax

```python
func.arrays_zip([1,2], ['a','b'])
```

## Analyze-Beispiele

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌───────────────────────────┐
│ [{1,'a'},{2,'b'},{3,'c'}] │
└───────────────────────────┘
```

## SQL-Syntax

```sql
ARRAYS_ZIP([1,2], ['a','b'])
```

## SQL-Beispiele

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);

┌───────────────────────────────────────────────────┐
│ [{"0":1,"1":"a"},{"0":2,"1":"b"},{"0":3,"1":"c"}] │
└───────────────────────────────────────────────────┘
```
