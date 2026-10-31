---
title: ARRAYS_ZIP (Lakehouse v2)
description: ARRAYS_ZIP — combina varias matrices en una matriz de estructuras.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-zip.md
---

Combina varias matrices en una matriz de estructuras.

## Sintaxis de Analyze

```python
func.arrays_zip([1,2], ['a','b'])
```

## Ejemplos de Analyze

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌───────────────────────────┐
│ [{1,'a'},{2,'b'},{3,'c'}] │
└───────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAYS_ZIP([1,2], ['a','b'])
```

## Ejemplos de SQL

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);

┌───────────────────────────────────────────────────┐
│ [{"0":1,"1":"a"},{"0":2,"1":"b"},{"0":3,"1":"c"}] │
└───────────────────────────────────────────────────┘
```
