---
title: SLICE (Lakehouse v1)
description: SLICE – extrahiert einen Ausschnitt aus dem Array anhand des Index (1-basiert).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/slice.md
---

Extrahiert einen Ausschnitt aus dem Array anhand des Index (1-basiert).

## Analyze-Syntax

```python
func.slice( <array>, <start>[, <end>] )
```

## Analyze-Beispiele

```python
func.slice([1, 21, 32, 4], 2, 3)

┌──────────────────────────────────┐
│ func.slice([1, 21, 32, 4], 2, 3) │
├──────────────────────────────────┤
│ [21,32]                          │ 
└──────────────────────────────────┘
```

## SQL-Syntax

```sql
SLICE( <array>, <start>[, <end>] )
```

## Aliasse

- [ARRAY_SLICE](../array-slice)

## SQL-Beispiele

```sql
SELECT ARRAY_SLICE([1, 21, 32, 4], 2, 3), SLICE([1, 21, 32, 4], 2, 3);

┌─────────────────────────────────────────────────────────────────┐
│ array_slice([1, 21, 32, 4], 2, 3) │ slice([1, 21, 32, 4], 2, 3) │
├───────────────────────────────────┼─────────────────────────────┤
│ [21,32]                           │ [21,32]                     │
└─────────────────────────────────────────────────────────────────┘
```
