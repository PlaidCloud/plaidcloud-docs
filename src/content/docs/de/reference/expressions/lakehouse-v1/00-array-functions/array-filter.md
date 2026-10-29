---
title: ARRAY_FILTER (Lakehouse v1)
description: ARRAY_FILTER – erstellt ein Array aus den Elementen des Eingabe-Arrays, für die die Lambda-Funktion true zurückgibt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-filter.md
---

Erstellt ein Array aus den Elementen des Eingabe-Arrays, für die die Lambda-Funktion true zurückgibt.

## Analyze-Syntax

```python
func.array_filter( <array>, <lambda> )
```

## Analyze-Beispiele

```python
func.array_filter([1, 2, 3], x -> (x > 1))

┌─────────────────────────────────────────────┐
│ func.array_filter([1, 2, 3], x -> (x > 1))  │
├─────────────────────────────────────────────┤
│ [2,3]                                       │
└─────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_FILTER( <array>, <lambda> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_FILTER([1, 2, 3], x -> x > 1);

┌───────────────────────────────────────┐
│ array_filter([1, 2, 3], x -> (x > 1)) │
├───────────────────────────────────────┤
│ [2,3]                                 │
└───────────────────────────────────────┘
```
