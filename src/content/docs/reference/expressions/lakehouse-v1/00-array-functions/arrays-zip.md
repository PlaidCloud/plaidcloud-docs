---
title: ARRAYS_ZIP
description: "Learn how to use the ARRAYS_ZIP array function in PlaidCloud Lakehouse. Merges multiple arrays into a single array tuple. Includes syntax and examples."
---

Merges multiple arrays into a single array tuple.

## Analyze Syntax

```python
func.arrays_zip( <array1> [, ...] )
```

## Analyze Examples

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## Arguments

| Arguments  | Description       |
|------------|-------------------|
| `<arrayN>` | The input ARRAYs. |

:::note
- The length of each array must be the same.
:::

## Return Type

Array(Tuple).

## SQL Examples

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```
