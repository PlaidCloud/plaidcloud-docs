---
title: RANGE (Lakehouse v1)
description: RANGE – gibt ein Array zurück, das aus dem Bereich [start, end) gebildet wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

Gibt ein Array zurück, das aus dem Bereich [start, end) gebildet wird.

## Analyze-Syntax

```python
func.range( <start>, <end> )
```

## Analyze-Beispiele

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## SQL-Syntax

```sql
RANGE( <start>, <end> )
```

## SQL-Beispiele

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
