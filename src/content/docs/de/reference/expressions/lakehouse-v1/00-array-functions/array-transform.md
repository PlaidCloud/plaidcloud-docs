---
title: ARRAY_TRANSFORM (Lakehouse v1)
description: ARRAY_TRANSFORM – gibt ein Array zurück, das sich aus der Anwendung der Lambda-Funktion auf jedes Element des Eingabe-Arrays ergibt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-transform.md
---

Gibt ein Array zurück, das sich aus der Anwendung der Lambda-Funktion auf jedes Element des Eingabe-Arrays ergibt.

## Analyze-Syntax

```python
func.array_transform( <array>, <lambda> )
```

## Analyze-Beispiele

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## Aliasse

- [ARRAY_APPLY](../array-apply)

## SQL-Beispiele

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
